# Netflix Recommendation System

A personalized movie recommendation system similar to Netflix, with its own custom API. The system uses three recommendation approaches:

1. **Content-Based Filtering** - Recommends movies similar to those you've liked based on features like genre, actors, etc.
2. **Collaborative Filtering** - Recommends movies that similar users have enjoyed
3. **Hybrid Approach** - Combines both approaches for better recommendations

## Features

- RESTful API built with FastAPI
- React frontend with Netflix-like UI
- Multiple recommendation algorithms
- Movie rating system
- User profiles with viewing history and preferences
- Responsive design

## Project Structure

```
netflix_recommendation_system/
├── api/                    # Backend API
│   └── main.py             # FastAPI main app
├── data/                   # Sample data
│   ├── movies.py           # Movie data
│   └── users.py            # User data and ratings
├── models/                 # Recommendation algorithms
│   └── recommendation.py   # Recommendation system implementation
├── frontend/               # React frontend
│   ├── public/
│   └── src/
│       ├── components/     # Reusable UI components
│       ├── pages/          # Page components
│       ├── App.js          # Main app component
│       ├── index.js        # Entry point
│       └── styles.css      # Global styles
├── requirements.txt        # Python dependencies
└── start.py                # Script to start both servers
```

## Setup and Installation

### Prerequisites

- Python 3.8+ 
- Node.js 14+ and npm
- Git

### Quick Start

The easiest way to run the application is to use the provided start script:

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install frontend dependencies:
   ```
   cd netflix_recommendation_system/frontend
   npm install
   cd ..
   ```

3. Run the start script:
   ```
   python start.py
   ```

   This will start both the backend and frontend servers and open the application in your browser.

### Manual Setup

If you prefer to start the servers manually:

#### Backend

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the backend server:
   ```
   cd netflix_recommendation_system
   uvicorn api.main:app --reload
   ```
   
   The API will be available at http://localhost:8000

4. Visit http://localhost:8000/docs to see the API documentation

#### Frontend

1. Navigate to the frontend directory:
   ```
   cd netflix_recommendation_system/frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```
   
   The frontend will be available at http://localhost:3000

## API Endpoints

- `GET /movies` - Get all movies
- `GET /movies/{movie_id}` - Get a specific movie
- `GET /users` - Get all users
- `GET /users/{user_id}` - Get a specific user
- `GET /recommendations/content-based/{user_id}` - Get content-based recommendations
- `GET /recommendations/collaborative/{user_id}` - Get collaborative filtering recommendations
- `GET /recommendations/hybrid/{user_id}` - Get hybrid recommendations (with optional content_weight parameter)
- `POST /ratings` - Add or update a movie rating

## Troubleshooting

### Images Not Loading
- The application uses placeholder URLs for images. In a real application, you would use actual image URLs.
- If images fail to load, the app will display a placeholder with the movie title.

### Bootstrap Dropdown Menu Not Working
- Make sure Bootstrap JavaScript is properly loaded.
- Check browser console for any JavaScript errors.

### API Connection Issues
- Ensure the backend server is running on port 8000.
- Check that CORS is properly configured.
- Verify your firewall is not blocking the connections.

### Rating Submission Errors
- Ratings must be between 0 and 5.
- You must be logged in to submit ratings.

## Future Improvements

- User authentication and registration
- Database integration (SQLite, PostgreSQL, etc.)
- More advanced recommendation algorithms
- Movie search functionality
- Personalized genre preferences
- Movie trailer integration
- Caching for better performance
- Deployment to a cloud service

## License

MIT 