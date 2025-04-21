import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { FaPlay, FaStar, FaArrowLeft } from 'react-icons/fa';
import MovieCard from '../components/MovieCard';

const MovieDetails = ({ user }) => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [movie, setMovie] = useState(null);
  const [similarMovies, setSimilarMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showRatingForm, setShowRatingForm] = useState(false);
  const [rating, setRating] = useState(0);
  const [ratingSubmitted, setRatingSubmitted] = useState(false);

  useEffect(() => {
    const fetchMovie = async () => {
      try {
        const response = await fetch(`http://localhost:8000/movies/${id}`);
        if (!response.ok) {
          throw new Error('Movie not found');
        }
        const data = await response.json();
        setMovie(data);
        
        // Fetch all movies to find similar ones (in a real app, this would be an API call)
        const allMoviesResponse = await fetch('http://localhost:8000/movies');
        if (!allMoviesResponse.ok) {
          throw new Error('Failed to fetch similar movies');
        }
        const allMovies = await allMoviesResponse.json();
        
        // Find movies with similar genres
        const similar = allMovies
          .filter(m => m.id !== data.id && m.genres.some(g => data.genres.includes(g)))
          .slice(0, 4);
          
        setSimilarMovies(similar);
        
      } catch (error) {
        console.error('Error fetching movie:', error);
        setError(error.message || 'Failed to load movie details');
      } finally {
        setIsLoading(false);
      }
    };

    fetchMovie();
    
    // Reset rating form on new movie load
    setShowRatingForm(false);
    setRating(0);
    setRatingSubmitted(false);
  }, [id, navigate]);

  const handleRateClick = () => {
    setShowRatingForm(prev => !prev);
  };

  const handleRatingChange = (value) => {
    setRating(value);
  };

  const handleRatingSubmit = async (e) => {
    e.preventDefault();
    
    if (!user) {
      alert('You must be logged in to rate movies');
      return;
    }
    
    try {
      const response = await fetch('http://localhost:8000/ratings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: user.id,
          movie_id: parseInt(id),
          rating: rating
        }),
      });
      
      if (!response.ok) {
        throw new Error('Server rejected the rating');
      }
      
      setRatingSubmitted(true);
      setTimeout(() => {
        setShowRatingForm(false);
      }, 2000);
    } catch (error) {
      console.error('Error submitting rating:', error);
      alert('Failed to submit rating. Please try again.');
    }
  };

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="spinner-border text-danger" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="alert alert-danger m-5" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
        <hr />
        <button 
          className="btn btn-outline-danger" 
          onClick={() => navigate('/')}
        >
          Return to Home
        </button>
      </div>
    );
  }

  return (
    <div className="movie-details-page">
      <button 
        className="btn btn-dark mb-4" 
        onClick={() => navigate(-1)}
      >
        <FaArrowLeft className="me-2" /> Back
      </button>
      
      <div className="movie-details">
        <img 
          src={movie.image_url} 
          alt={movie.title} 
          className="movie-poster-large"
          onError={(e) => {
            e.target.onerror = null;
            e.target.src = 'https://placehold.co/300x450/181818/ffffff?text=' + encodeURIComponent(movie.title);
          }}
        />
        
        <div className="movie-details-content">
          <h1 className="movie-detail-title">{movie.title}</h1>
          
          <div className="movie-metadata">
            <span className="movie-year">{movie.year}</span>
            <span className="movie-duration">{movie.duration}</span>
            <span className="movie-rating">
              <FaStar className="rating-icon" /> {movie.rating.toFixed(1)}
            </span>
          </div>
          
          <div className="movie-genres mb-4">
            {movie.genres.map(genre => (
              <span key={genre} className="badge bg-dark me-2">
                {genre}
              </span>
            ))}
          </div>
          
          <p className="movie-detail-description">{movie.description}</p>
          
          <div className="mb-3">
            <strong>Director:</strong> {movie.director}
          </div>
          
          <div className="action-buttons">
            <button className="btn btn-play">
              <FaPlay /> Play
            </button>
            <button className="btn btn-rate" onClick={handleRateClick}>
              <FaStar /> Rate
            </button>
          </div>
          
          {showRatingForm && (
            <div className="rating-form">
              <h3 className="mb-3">Rate this title</h3>
              {ratingSubmitted ? (
                <div className="alert alert-success">Rating submitted successfully!</div>
              ) : (
                <form onSubmit={handleRatingSubmit}>
                  <div className="mb-3">
                    <div className="rating-stars d-flex gap-2 mb-3">
                      {[1, 2, 3, 4, 5].map(value => (
                        <FaStar 
                          key={value}
                          className={`fs-3 ${value <= rating ? 'text-warning' : 'text-secondary'}`}
                          style={{ cursor: 'pointer' }}
                          onClick={() => handleRatingChange(value)}
                        />
                      ))}
                    </div>
                    <div className="text-muted mb-3">
                      {rating === 0 ? 'Click to rate' : `Your rating: ${rating}/5`}
                    </div>
                  </div>
                  <button 
                    type="submit" 
                    className="btn btn-primary me-2"
                    disabled={rating === 0}
                  >
                    Submit
                  </button>
                  <button 
                    type="button" 
                    className="btn btn-secondary"
                    onClick={() => setShowRatingForm(false)}
                  >
                    Cancel
                  </button>
                </form>
              )}
            </div>
          )}
        </div>
      </div>
      
      {similarMovies.length > 0 && (
        <div className="similar-movies mt-5">
          <h2 className="section-title">More Like This</h2>
          <div className="movie-carousel">
            {similarMovies.map(movie => (
              <MovieCard key={movie.id} movie={movie} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default MovieDetails; 