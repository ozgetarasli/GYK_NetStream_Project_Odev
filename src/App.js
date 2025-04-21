import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';

// Components
import Navbar from './components/Navbar';
import Home from './pages/Home';
import MovieDetails from './pages/MovieDetails';
import Profile from './pages/Profile';
import Recommendations from './pages/Recommendations';

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // For demo purposes, we'll automatically log in as user 1
    const fetchUser = async () => {
      try {
        const response = await fetch('http://localhost:8000/users/1');
        const userData = await response.json();
        setCurrentUser(userData);
      } catch (error) {
        console.error('Error fetching user:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUser();
  }, []);

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
    <Router>
      <div className="app">
        <Navbar user={currentUser} />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home user={currentUser} />} />
            <Route path="/movie/:id" element={<MovieDetails user={currentUser} />} />
            <Route path="/profile" element={
              currentUser ? <Profile user={currentUser} /> : <Navigate to="/" />
            } />
            <Route path="/recommendations" element={
              currentUser ? <Recommendations user={currentUser} /> : <Navigate to="/" />
            } />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App; 