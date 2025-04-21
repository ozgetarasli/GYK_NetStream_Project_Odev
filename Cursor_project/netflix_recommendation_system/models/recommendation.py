"""
Recommendation system for Netflix-like app
Includes both content-based and collaborative filtering approaches
"""

import numpy as np
from collections import defaultdict
from .cosine_similarity import cosine_similarity

class RecommendationSystem:
    def __init__(self, movies, users, ratings):
        self.movies = movies
        self.users = users
        self.ratings = ratings
        
        # Create a user-movie rating matrix
        self.user_movie_matrix = self._create_user_movie_matrix()
        # Create a movie similarity matrix
        self.movie_similarity_matrix = self._create_movie_similarity_matrix()
        
    def _create_user_movie_matrix(self):
        """
        Create a user-movie rating matrix for collaborative filtering
        """
        # Get unique user IDs and movie IDs
        user_ids = set(user['id'] for user in self.users)
        movie_ids = set(movie['id'] for movie in self.movies)
        
        # Initialize matrix with zeros
        matrix = np.zeros((max(user_ids), max(movie_ids)))
        
        # Fill in the matrix with ratings
        for rating in self.ratings:
            user_id = rating['user_id']
            movie_id = rating['movie_id']
            score = rating['rating']
            matrix[user_id-1, movie_id-1] = score
            
        return matrix
    
    def _create_movie_similarity_matrix(self):
        """
        Create a movie similarity matrix based on feature vectors
        """
        # Extract feature vectors for each movie
        feature_vectors = np.array([movie['features'] for movie in self.movies])
        
        # Calculate cosine similarity between movies
        return cosine_similarity(feature_vectors)
    
    def content_based_recommendations(self, user_id, n=5):
        """
        Generate content-based recommendations for a user
        based on their preferences and liked movies
        """
        # Find the user
        user = next((u for u in self.users if u['id'] == user_id), None)
        if not user:
            return []
        
        # Get movies the user has already viewed
        viewed_movie_ids = set(user['viewed_movies'])
        
        # Get user's preferred genres
        preferred_genres = set(user['preferences']['genres'])
        min_rating = user['preferences']['min_rating']
        
        # Filter movies by preferred genres and minimum rating
        candidate_movies = []
        for movie in self.movies:
            if (movie['id'] not in viewed_movie_ids and 
                movie['rating'] >= min_rating and
                any(genre in preferred_genres for genre in movie['genres'])):
                candidate_movies.append(movie)
        
        # If no candidate movies, return empty list
        if not candidate_movies:
            return []
        
        # Score candidate movies based on similarity to liked movies
        movie_scores = defaultdict(float)
        for liked_movie_id in user['liked_movies']:
            # Get the index of the liked movie
            liked_idx = next((i for i, movie in enumerate(self.movies) if movie['id'] == liked_movie_id), None)
            if liked_idx is None:
                continue
                
            # Get similarity scores between the liked movie and all candidate movies
            for candidate in candidate_movies:
                candidate_idx = next((i for i, movie in enumerate(self.movies) if movie['id'] == candidate['id']), None)
                if candidate_idx is None:
                    continue
                
                similarity = self.movie_similarity_matrix[liked_idx, candidate_idx]
                movie_scores[candidate['id']] += similarity
        
        # Sort candidate movies by score
        ranked_movies = sorted(
            [(movie_id, score) for movie_id, score in movie_scores.items()],
            key=lambda x: x[1],
            reverse=True
        )
        
        # Get the top n movies
        top_movie_ids = [movie_id for movie_id, _ in ranked_movies[:n]]
        
        # Return the movie objects
        return [next(movie for movie in self.movies if movie['id'] == movie_id) for movie_id in top_movie_ids]
    
    def collaborative_filtering_recommendations(self, user_id, n=5):
        """
        Generate collaborative filtering recommendations for a user
        based on similar users' ratings
        """
        # Find the user index
        user_idx = user_id - 1
        
        # Get movies the user has already viewed
        user = next((u for u in self.users if u['id'] == user_id), None)
        if not user:
            return []
        
        viewed_movie_ids = set(user['viewed_movies'])
        
        # Calculate similarity between the target user and all other users
        user_matrix = self.user_movie_matrix
        target_user_vector = user_matrix[user_idx].reshape(1, -1)
        user_similarity = cosine_similarity(target_user_vector, user_matrix)[0]
        
        # Get the indices of the most similar users (excluding the target user)
        similar_users_indices = np.argsort(user_similarity)[::-1]
        similar_users_indices = similar_users_indices[similar_users_indices != user_idx][:10]  # Top 10 similar users
        
        # Calculate predicted ratings for unwatched movies
        predicted_ratings = {}
        for movie_id in range(1, self.user_movie_matrix.shape[1] + 1):
            if movie_id not in viewed_movie_ids:
                # Get ratings from similar users for this movie
                movie_idx = movie_id - 1
                similar_user_ratings = []
                similar_user_weights = []
                
                for similar_user_idx in similar_users_indices:
                    rating = self.user_movie_matrix[similar_user_idx, movie_idx]
                    if rating > 0:  # Only consider if the user has rated the movie
                        similar_user_ratings.append(rating)
                        similar_user_weights.append(user_similarity[similar_user_idx])
                
                # Calculate weighted average rating
                if similar_user_ratings:
                    predicted_rating = np.average(similar_user_ratings, weights=similar_user_weights)
                    predicted_ratings[movie_id] = predicted_rating
        
        # Sort movies by predicted rating
        ranked_movies = sorted(
            predicted_ratings.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Get the top n movies
        top_movie_ids = [movie_id for movie_id, _ in ranked_movies[:n]]
        
        # Return the movie objects
        return [next(movie for movie in self.movies if movie['id'] == movie_id) for movie_id in top_movie_ids]
    
    def hybrid_recommendations(self, user_id, n=5, content_weight=0.5):
        """
        Generate hybrid recommendations combining content-based and collaborative filtering
        """
        # Get recommendations from both methods
        content_recs = self.content_based_recommendations(user_id, n=n)
        collab_recs = self.collaborative_filtering_recommendations(user_id, n=n)
        
        # Combine the recommendations using a weighted approach
        movie_scores = defaultdict(float)
        
        # Add scores from content-based recommendations
        for i, movie in enumerate(content_recs):
            movie_scores[movie['id']] += content_weight * (n - i) / n
        
        # Add scores from collaborative filtering recommendations
        for i, movie in enumerate(collab_recs):
            movie_scores[movie['id']] += (1 - content_weight) * (n - i) / n
        
        # Sort movies by score
        ranked_movies = sorted(
            [(movie_id, score) for movie_id, score in movie_scores.items()],
            key=lambda x: x[1],
            reverse=True
        )
        
        # Get the top n movies
        top_movie_ids = [movie_id for movie_id, _ in ranked_movies[:n]]
        
        # Return the movie objects
        return [next(movie for movie in self.movies if movie['id'] == movie_id) for movie_id in top_movie_ids] 