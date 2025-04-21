"""
Basic start script for Netflix Recommendation API
"""

import sys
import os
import subprocess
import time
import webbrowser

def main():
    print("Starting Netflix Recommendation API...")
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Start the API server
        print("Starting API server...")
        subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "api.main:app", "--reload"],
            cwd=current_dir
        )
        
        # Wait for the server to start
        time.sleep(3)
        
        # Open browser
        print("Opening browser...")
        webbrowser.open("http://localhost:8000")
        
        print("\nAPI is running at http://localhost:8000")
        print("Press Ctrl+C to stop the server")
        
        # Keep the script running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping server...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 