"""
Sample user data for Netflix recommendation system
"""

users = [
    {
        "id": 1,
        "username": "john_doe",
        "name": "John Doe",
        "email": "john@example.com",
        "viewed_movies": [1, 3, 5, 8],
        "liked_movies": [1, 5],
        "preferences": {
            "genres": ["Sci-Fi", "Thriller", "Crime"],
            "min_rating": 7.5
        }
    },
    {
        "id": 2,
        "username": "jane_smith",
        "name": "Jane Smith",
        "email": "jane@example.com",
        "viewed_movies": [2, 4, 7, 10],
        "liked_movies": [2, 7],
        "preferences": {
            "genres": ["Drama", "Biography", "Fantasy"],
            "min_rating": 8.0
        }
    },
    {
        "id": 3,
        "username": "mike_jones",
        "name": "Mike Jones",
        "email": "mike@example.com",
        "viewed_movies": [3, 5, 9],
        "liked_movies": [5, 9],
        "preferences": {
            "genres": ["Crime", "Biography", "Drama"],
            "min_rating": 8.5
        }
    },
    {
        "id": 4,
        "username": "sarah_lee",
        "name": "Sarah Lee",
        "email": "sarah@example.com",
        "viewed_movies": [1, 6, 8],
        "liked_movies": [6, 8],
        "preferences": {
            "genres": ["Sci-Fi", "Mystery", "Drama"],
            "min_rating": 8.0
        }
    },
    {
        "id": 5,
        "username": "david_kim",
        "name": "David Kim",
        "email": "david@example.com",
        "viewed_movies": [4, 6, 10],
        "liked_movies": [4],
        "preferences": {
            "genres": ["Fantasy", "Sci-Fi", "Adventure"],
            "min_rating": 7.0
        }
    }
]

# Sample user ratings (user_id, movie_id, rating)
ratings = [
    {"user_id": 1, "movie_id": 1, "rating": 4.5},
    {"user_id": 1, "movie_id": 3, "rating": 3.0},
    {"user_id": 1, "movie_id": 5, "rating": 5.0},
    {"user_id": 1, "movie_id": 8, "rating": 3.5},
    
    {"user_id": 2, "movie_id": 2, "rating": 5.0},
    {"user_id": 2, "movie_id": 4, "rating": 3.5},
    {"user_id": 2, "movie_id": 7, "rating": 4.5},
    {"user_id": 2, "movie_id": 10, "rating": 2.5},
    
    {"user_id": 3, "movie_id": 3, "rating": 3.5},
    {"user_id": 3, "movie_id": 5, "rating": 4.5},
    {"user_id": 3, "movie_id": 9, "rating": 5.0},
    
    {"user_id": 4, "movie_id": 1, "rating": 3.0},
    {"user_id": 4, "movie_id": 6, "rating": 4.5},
    {"user_id": 4, "movie_id": 8, "rating": 5.0},
    
    {"user_id": 5, "movie_id": 4, "rating": 5.0},
    {"user_id": 5, "movie_id": 6, "rating": 3.5},
    {"user_id": 5, "movie_id": 10, "rating": 2.0}
] 