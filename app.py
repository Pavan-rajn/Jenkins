# app.py

import os
from datetime import datetime

def print_status():
    """Prints a simple status message."""
    
    # Get the image tag from the environment variable set during the Docker build
    image_tag = os.environ.get('IMAGE_TAG', 'unknown_tag')
    
    print(f"--- Application Status ---")
    print(f"Hello, World! I am running inside a Docker container.")
    print(f"Built Jenkins Tag: {image_tag}")
    print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"--------------------------")

if __name__ == "__main__":
    print_status()
