# Troubleshooting Guide

## Fixing Import Errors

If you're seeing import errors like these:

```
Import "fastapi" could not be resolved
Import "fastapi.middleware.cors" could not be resolved
Import "fastapi.responses" could not be resolved
Import "pydantic" could not be resolved
Import "uvicorn" could not be resolved
Import "sklearn.metrics.pairwise" could not be resolved
```

Try these solutions:

### 1. Install Required Packages

First, make sure you have all the required packages installed:

```bash
pip install fastapi uvicorn scikit-learn numpy pydantic requests
```

### 2. Custom Implementations

The project includes custom implementations to work around dependency issues:

- `models/cosine_similarity.py` provides a custom implementation of cosine similarity without requiring sklearn.metrics.pairwise
- The main.py file has been updated to use more reliable imports

### 3. Running the API Server

Use one of these methods to run the API server:

#### Simple Method (Recommended)

Run the basic Python start script:

```bash
python start_basic.py
```

This will start the API server and open your browser to http://localhost:8000.

#### Manual Method

Start the API server manually:

```bash
cd netflix_recommendation_system
python -m uvicorn api.main:app --reload
```

#### Windows Batch File

For Windows users, you can also use the batch file:

```bash
.\start_windows.bat
```

### 4. IDE-specific Issues

If you're using an IDE like VS Code or PyCharm:

1. Make sure your IDE is using the correct Python interpreter with the installed packages
2. Try restarting your IDE or reload the window
3. Configure your IDE to include the project root directory in the Python path

### 5. Module Import Issues

If you're still seeing import errors for custom modules:

1. Make sure you have `__init__.py` files in each directory (api, models, data)
2. Try using absolute imports instead of relative imports
3. Make sure your Python path includes the project root directory

### 6. Testing the API

To test if the API is working correctly:

1. Open your browser to http://localhost:8000
2. You should see a message: "Welcome to Netflix Recommendation API"
3. Visit http://localhost:8000/docs to see the API documentation

If you're still experiencing issues, please check the error logs for more details. 