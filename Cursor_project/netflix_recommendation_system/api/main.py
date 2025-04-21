from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator
from typing import List, Optional, Dict, Any

import sys
import os

# Add the parent directory to sys.path to allow imports from sibling directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.recommendation import RecommendationSystem
from data.movies import movies
from data.users import users, ratings

# Initialize the FastAPI app
app = FastAPI(
    title="Netflix Recommendation API",
    description="API for movie recommendations similar to Netflix",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the recommendation system
recommendation_system = RecommendationSystem(movies, users, ratings)

# Define pydantic models for request/response validation
class Movie(BaseModel):
    id: int
    title: str
    genres: List[str]
    description: str
    year: int
    director: str
    rating: float
    duration: str
    image_url: str

class User(BaseModel):
    id: int
    username: str
    name: str
    email: str
    viewed_movies: List[int]
    liked_movies: List[int]
    preferences: Dict[str, Any]

class MovieRating(BaseModel):
    user_id: int
    movie_id: int
    rating: float
    
    @field_validator('rating')
    @classmethod
    def rating_must_be_valid(cls, v):
        if v < 0 or v > 5:
            raise ValueError('Rating must be between 0 and 5')
        return v

# Exception handler for validation errors
@app.exception_handler(ValueError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)},
    )

# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to Netflix Recommendation API"}

@app.get("/movies", response_model=List[Movie])
def get_movies():
    return movies

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/recommendations/content-based/{user_id}", response_model=List[Movie])
def get_content_based_recommendations(
    user_id: int,
    n: int = 5
):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        recommendations = recommendation_system.content_based_recommendations(user_id, n)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/recommendations/collaborative/{user_id}", response_model=List[Movie])
def get_collaborative_recommendations(
    user_id: int,
    n: int = 5
):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        recommendations = recommendation_system.collaborative_filtering_recommendations(user_id, n)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/recommendations/hybrid/{user_id}", response_model=List[Movie])
def get_hybrid_recommendations(
    user_id: int,
    n: int = 5,
    content_weight: float = 0.5
):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if content_weight < 0 or content_weight > 1:
        raise HTTPException(status_code=400, detail="Content weight must be between 0 and 1")
    
    try:
        recommendations = recommendation_system.hybrid_recommendations(user_id, n, content_weight)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.post("/ratings", status_code=201)
def add_rating(rating: MovieRating):
    # Check if user exists
    user = next((user for user in users if user["id"] == rating.user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if movie exists
    movie = next((movie for movie in movies if movie["id"] == rating.movie_id), None)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    try:
        # Check if rating already exists
        existing_rating = next((r for r in ratings if r["user_id"] == rating.user_id and r["movie_id"] == rating.movie_id), None)
        if existing_rating:
            # Update existing rating
            existing_rating["rating"] = rating.rating
        else:
            # Add new rating
            ratings.append(rating.model_dump())
        
        # Add to viewed movies if not already there
        if rating.movie_id not in user["viewed_movies"]:
            user["viewed_movies"].append(rating.movie_id)
        
        # Add to liked movies if rating is high (4.0 or higher)
        if rating.rating >= 4.0 and rating.movie_id not in user["liked_movies"]:
            user["liked_movies"].append(rating.movie_id)
        elif rating.rating < 4.0 and rating.movie_id in user["liked_movies"]:
            user["liked_movies"].remove(rating.movie_id)
        
        # Reinitialize the recommendation system with updated data
        global recommendation_system
        recommendation_system = RecommendationSystem(movies, users, ratings)
        
        return {"message": "Rating added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding rating: {str(e)}")

# Run with: uvicorn api.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 