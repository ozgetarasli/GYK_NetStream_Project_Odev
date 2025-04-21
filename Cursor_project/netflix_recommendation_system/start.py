"""
Script to start both the backend and frontend servers
"""

import subprocess
import sys
import os
import time
import webbrowser
from threading import Thread

def start_backend():
    print("Starting backend server...")
    backend_process = subprocess.Popen(
        ["python", "-m", "uvicorn", "api.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    return backend_process

def start_frontend():
    print("Starting frontend server...")
    frontend_process = subprocess.Popen(
        ["npm", "start"],
        cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
    )
    return frontend_process

def wait_for_backend(url="http://localhost:8000", timeout=30):
    import requests
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.5)
    return False

def open_browser():
    # Wait for the backend to start
    if wait_for_backend():
        print("Backend is ready!")
        # Open the frontend in a browser
        time.sleep(5)  # Give frontend time to initialize
        print("Opening browser...")
        webbrowser.open("http://localhost:3000")
    else:
        print("Backend failed to start within the timeout period.")

if __name__ == "__main__":
    try:
        # Start the backend
        backend_process = start_backend()
        
        # Start the frontend
        frontend_process = start_frontend()
        
        # Open browser in a separate thread
        browser_thread = Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Keep the main process running until user interrupts
        print("\nPress Ctrl+C to stop both servers...\n")
        backend_process.wait()
        
    except KeyboardInterrupt:
        print("\nStopping servers...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure processes are terminated
        try:
            if 'backend_process' in locals():
                backend_process.terminate()
            if 'frontend_process' in locals():
                frontend_process.terminate()
        except:
            pass
        print("Servers have been stopped.") 