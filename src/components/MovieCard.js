import React from 'react';
import { useNavigate } from 'react-router-dom';
import { FaStar } from 'react-icons/fa';

const MovieCard = ({ movie }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/movie/${movie.id}`);
  };

  return (
    <div className="movie-card" onClick={handleClick}>
      <img 
        src={movie.image_url} 
        alt={movie.title} 
        className="movie-poster"
        onError={(e) => {
          e.target.onerror = null;
          e.target.src = 'https://placehold.co/200x300/181818/ffffff?text=' + encodeURIComponent(movie.title);
        }}
      />
      <div className="movie-info">
        <h3 className="movie-title">{movie.title}</h3>
        <div className="movie-genre">
          {movie.genres.slice(0, 2).join(' • ')}
          {movie.genres.length > 2 && ' • ...'}
        </div>
        <div className="movie-rating">
          <FaStar className="rating-icon" />
          <span>{movie.rating.toFixed(1)}</span>
        </div>
      </div>
    </div>
  );
};

export default MovieCard; 