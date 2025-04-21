import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FaUser, FaSearch } from 'react-icons/fa';

const Navbar = ({ user }) => {
  const [scrolled, setScrolled] = useState(false);
  
  useEffect(() => {
    const handleScroll = () => {
      const isScrolled = window.scrollY > 50;
      if (isScrolled !== scrolled) {
        setScrolled(isScrolled);
      }
    };

    window.addEventListener('scroll', handleScroll);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [scrolled]);

  return (
    <nav className={`navbar navbar-expand-lg ${scrolled ? 'scrolled' : ''}`}>
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">NETSTREAM</Link>
        
        <button 
          className="navbar-toggler" 
          type="button" 
          data-bs-toggle="collapse" 
          data-bs-target="#navbarContent"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        
        <div className="collapse navbar-collapse" id="navbarContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/recommendations">Recommendations</Link>
            </li>
          </ul>
          
          <div className="d-flex align-items-center">
            <div className="search-box me-3">
              <div className="input-group">
                <span className="input-group-text bg-dark border-dark text-light">
                  <FaSearch />
                </span>
                <input 
                  type="text" 
                  className="form-control bg-dark border-dark text-light" 
                  placeholder="Search..." 
                />
              </div>
            </div>
            
            {user && (
              <div className="dropdown profile-dropdown">
                <button 
                  className="btn btn-dark dropdown-toggle" 
                  type="button" 
                  id="profileDropdown" 
                  data-bs-toggle="dropdown" 
                  aria-expanded="false"
                >
                  <FaUser className="me-2" />
                  {user.name}
                </button>
                <ul className="dropdown-menu" aria-labelledby="profileDropdown">
                  <li>
                    <Link className="dropdown-item" to="/profile">Profile</Link>
                  </li>
                  <li>
                    <hr className="dropdown-divider" />
                  </li>
                  <li>
                    <button className="dropdown-item">Logout</button>
                  </li>
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 