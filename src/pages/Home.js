import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FaPlay, FaInfo } from 'react-icons/fa';
import MovieCard from '../components/MovieCard';

const Home = ({ user }) => {
  const [featuredMovie, setFeaturedMovie] = useState(null);
  const [allMovies, setAllMovies] = useState([]);
  const [trendingMovies, setTrendingMovies] = useState([]);
  const [recommendedMovies, setRecommendedMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await fetch('http://localhost:8000/movies');
        if (!response.ok) {
          throw new Error('Failed to fetch movies');
        }
        const data = await response.json();
        
        setAllMovies(data);
        
        // Set a random movie as featured
        const randomIndex = Math.floor(Math.random() * data.length);
        setFeaturedMovie(data[randomIndex]);
        
        // Set trending movies (for demo, we'll just sort by rating)
        const sorted = [...data].sort((a, b) => b.rating - a.rating);
        setTrendingMovies(sorted.slice(0, 5));
        
      } catch (error) {
        console.error('Error fetching movies:', error);
        setError('Failed to load movies. Please try again later.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchMovies();
  }, []);

  // Get personalized recommendations if user is logged in
  useEffect(() => {
    if (user) {
      const fetchRecommendations = async () => {
        try {
          const response = await fetch(`http://localhost:8000/recommendations/hybrid/${user.id}`);
          if (!response.ok) {
            throw new Error('Failed to fetch recommendations');
          }
          const data = await response.json();
          setRecommendedMovies(data);
        } catch (error) {
          console.error('Error fetching recommendations:', error);
          // Fall back to unviewed movies if recommendations fail
          const unviewedMovies = allMovies.filter(movie => !user.viewed_movies.includes(movie.id));
          setRecommendedMovies(unviewedMovies.slice(0, 5));
        }
      };

      fetchRecommendations();
    }
  }, [user, allMovies]);

  if (isLoading || !featuredMovie) {
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
        {error}
      </div>
    );
  }

  return (
    <div className="home-page">
      {/* Hero Section with Featured Movie */}
      <div 
        className="hero-section" 
        style={{ 
          backgroundImage: `url(${featuredMovie.image_url})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center'
        }}
      >
        <div className="hero-content">
          <h1 className="hero-title">{featuredMovie.title}</h1>
          <p className="hero-description">{featuredMovie.description}</p>
          <div className="d-flex">
            <Link to={`/movie/${featuredMovie.id}`} className="btn btn-light me-3">
              <FaPlay className="me-2" /> Play
            </Link>
            <Link to={`/movie/${featuredMovie.id}`} className="btn btn-secondary">
              <FaInfo className="me-2" /> More Info
            </Link>
          </div>
        </div>
      </div>

      {/* Trending Now Section */}
      <div className="movie-section">
        <h2 className="section-title">Trending Now</h2>
        <div className="movie-carousel">
          {trendingMovies.map(movie => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      </div>

      {/* Personalized Recommendations Section */}
      {user && (
        <div className="movie-section">
          <h2 className="section-title">Recommended for You</h2>
          <div className="movie-carousel">
            {recommendedMovies.length > 0 ? (
              recommendedMovies.map(movie => (
                <MovieCard key={movie.id} movie={movie} />
              ))
            ) : (
              <p className="text-muted">No recommendations available yet. Try rating more movies!</p>
            )}
          </div>
        </div>
      )}

      {/* All Movies Section */}
      <div className="movie-section">
        <h2 className="section-title">All Movies</h2>
        <div className="movie-carousel">
          {allMovies.map(movie => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home; 