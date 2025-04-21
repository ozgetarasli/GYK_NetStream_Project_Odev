import React, { useState, useEffect } from 'react';
import MovieCard from '../components/MovieCard';

const Recommendations = ({ user }) => {
  const [activeTab, setActiveTab] = useState('hybrid');
  const [contentRecommendations, setContentRecommendations] = useState([]);
  const [collaborativeRecommendations, setCollaborativeRecommendations] = useState([]);
  const [hybridRecommendations, setHybridRecommendations] = useState([]);
  const [contentWeight, setContentWeight] = useState(0.5);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchRecommendations = async () => {
      if (!user) return;
      
      setIsLoading(true);
      
      try {
        // Fetch content-based recommendations
        const contentResponse = await fetch(`http://localhost:8000/recommendations/content-based/${user.id}`);
        const contentData = await contentResponse.json();
        setContentRecommendations(contentData);
        
        // Fetch collaborative filtering recommendations
        const collabResponse = await fetch(`http://localhost:8000/recommendations/collaborative/${user.id}`);
        const collabData = await collabResponse.json();
        setCollaborativeRecommendations(collabData);
        
        // Fetch hybrid recommendations
        const hybridResponse = await fetch(
          `http://localhost:8000/recommendations/hybrid/${user.id}?content_weight=${contentWeight}`
        );
        const hybridData = await hybridResponse.json();
        setHybridRecommendations(hybridData);
        
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchRecommendations();
  }, [user, contentWeight]);

  const handleWeightChange = (e) => {
    setContentWeight(parseFloat(e.target.value));
  };

  if (!user) {
    return (
      <div className="alert alert-warning">
        Please log in to see your personalized recommendations.
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
    <div className="recommendations-page">
      <h1 className="mb-4">Your Personalized Recommendations</h1>
      
      <div className="recommendation-tabs">
        <ul className="nav nav-pills mb-4">
          <li className="nav-item">
            <button 
              className={`nav-link ${activeTab === 'hybrid' ? 'active' : ''}`}
              onClick={() => setActiveTab('hybrid')}
            >
              Hybrid Recommendations
            </button>
          </li>
          <li className="nav-item">
            <button 
              className={`nav-link ${activeTab === 'content' ? 'active' : ''}`}
              onClick={() => setActiveTab('content')}
            >
              Content-Based
            </button>
          </li>
          <li className="nav-item">
            <button 
              className={`nav-link ${activeTab === 'collaborative' ? 'active' : ''}`}
              onClick={() => setActiveTab('collaborative')}
            >
              Collaborative Filtering
            </button>
          </li>
        </ul>
      </div>
      
      {activeTab === 'hybrid' && (
        <div className="hybrid-recommendations">
          <div className="content-weight-slider mb-4">
            <label htmlFor="contentWeight" className="form-label">
              Recommendation Balance: {(contentWeight * 100).toFixed(0)}% Content-Based / {((1 - contentWeight) * 100).toFixed(0)}% Collaborative
            </label>
            <input 
              type="range" 
              className="form-range" 
              min="0" 
              max="1" 
              step="0.1" 
              id="contentWeight"
              value={contentWeight}
              onChange={handleWeightChange}
            />
          </div>
          
          <div className="movie-grid row">
            {hybridRecommendations.length > 0 ? (
              hybridRecommendations.map(movie => (
                <div key={movie.id} className="col-md-4 col-lg-3 mb-4">
                  <MovieCard movie={movie} />
                </div>
              ))
            ) : (
              <div className="col-12">
                <div className="alert alert-info">
                  No hybrid recommendations available. Try adjusting the balance or rating more movies.
                </div>
              </div>
            )}
          </div>
        </div>
      )}
      
      {activeTab === 'content' && (
        <div className="content-recommendations">
          <p className="mb-4">
            Content-based recommendations are based on movies similar to ones you've enjoyed 
            and match your genre preferences.
          </p>
          
          <div className="movie-grid row">
            {contentRecommendations.length > 0 ? (
              contentRecommendations.map(movie => (
                <div key={movie.id} className="col-md-4 col-lg-3 mb-4">
                  <MovieCard movie={movie} />
                </div>
              ))
            ) : (
              <div className="col-12">
                <div className="alert alert-info">
                  No content-based recommendations available. Try rating more movies or updating your preferences.
                </div>
              </div>
            )}
          </div>
        </div>
      )}
      
      {activeTab === 'collaborative' && (
        <div className="collaborative-recommendations">
          <p className="mb-4">
            Collaborative filtering recommendations are based on what similar users have enjoyed.
          </p>
          
          <div className="movie-grid row">
            {collaborativeRecommendations.length > 0 ? (
              collaborativeRecommendations.map(movie => (
                <div key={movie.id} className="col-md-4 col-lg-3 mb-4">
                  <MovieCard movie={movie} />
                </div>
              ))
            ) : (
              <div className="col-12">
                <div className="alert alert-info">
                  No collaborative recommendations available. Try rating more movies to improve results.
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default Recommendations; 