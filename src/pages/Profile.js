import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FaUser } from 'react-icons/fa';
import MovieCard from '../components/MovieCard';

const Profile = ({ user }) => {
  const [viewedMovies, setViewedMovies] = useState([]);
  const [likedMovies, setLikedMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchMovies = async () => {
      if (!user) return;
      
      setIsLoading(true);
      
      try {
        // Fetch all movies
        const response = await fetch('http://localhost:8000/movies');
        const movies = await response.json();
        
        // Filter viewed and liked movies
        const viewed = movies.filter(movie => user.viewed_movies.includes(movie.id));
        const liked = movies.filter(movie => user.liked_movies.includes(movie.id));
        
        setViewedMovies(viewed);
        setLikedMovies(liked);
      } catch (error) {
        console.error('Error fetching movies:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchMovies();
  }, [user]);

  if (!user) {
    return (
      <div className="alert alert-warning">
        Please log in to view your profile.
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="spinner-border text-danger" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="profile-page">
      <div className="profile-header">
        <div className="profile-avatar">
          <FaUser />
        </div>
        <div>
          <h1 className="profile-name">{user.name}</h1>
          <p className="profile-email">{user.email}</p>
        </div>
      </div>
      
      <div className="profile-section">
        <h2 className="profile-section-title">Your Preferences</h2>
        <div className="preferences-container">
          <div className="mb-3">
            <strong>Favorite Genres:</strong>
            <div className="mt-2">
              {user.preferences.genres.map(genre => (
                <span key={genre} className="preference-tag">
                  {genre}
                </span>
              ))}
            </div>
          </div>
          <div>
            <strong>Minimum Rating:</strong> {user.preferences.min_rating}
          </div>
        </div>
      </div>
      
      <div className="profile-section">
        <h2 className="profile-section-title">Movies You Liked</h2>
        {likedMovies.length > 0 ? (
          <div className="movie-carousel">
            {likedMovies.map(movie => (
              <MovieCard key={movie.id} movie={movie} />
            ))}
          </div>
        ) : (
          <p>You haven't liked any movies yet. Start rating movies to see them here!</p>
        )}
      </div>
      
      <div className="profile-section">
        <h2 className="profile-section-title">Recently Viewed</h2>
        {viewedMovies.length > 0 ? (
          <div className="movie-carousel">
            {viewedMovies.map(movie => (
              <MovieCard key={movie.id} movie={movie} />
            ))}
          </div>
        ) : (
          <p>You haven't viewed any movies yet.</p>
        )}
      </div>
      
      <div className="profile-section">
        <h2 className="profile-section-title">Personalized Recommendations</h2>
        <p>
          Get personalized movie recommendations based on your viewing history and preferences.
        </p>
        <Link to="/recommendations" className="btn btn-danger mt-2">
          See Your Recommendations
        </Link>
      </div>
    </div>
  );
};

export default Profile; 