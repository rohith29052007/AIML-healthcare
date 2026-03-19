"""
Google Drive Model Downloader
Downloads pre-trained models from Google Drive
"""

import os
import requests
from pathlib import Path

def download_from_google_drive(file_id, output_path):
    """
    Download a file from Google Drive using its file ID
    
    Args:
        file_id: Google Drive file ID (from shareable link)
        output_path: Local path to save the file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Google Drive direct download URL with confirmation bypass
        url = f"https://drive.google.com/uc?id={file_id}&export=download&confirm=t"
        
        print(f"Downloading model from Google Drive: {file_id}")
        
        # Download with streaming and timeout
        session = requests.Session()
        response = session.get(url, stream=True, timeout=300)
        response.raise_for_status()
        
        # Get actual file size
        total_size = int(response.headers.get('content-length', 0))
        
        if total_size == 0:
            print("⚠ Warning: Could not determine file size. File may be corrupted or download failed.")
            return False
        
        print(f"File size: {total_size / 1024 / 1024:.1f}MB")
        
        # Save file
        downloaded = 0
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"  Progress: {percent:.1f}% ({downloaded / 1024 / 1024:.1f}MB / {total_size / 1024 / 1024:.1f}MB)", end='\r')
        
        print(f"\n✓ Model downloaded successfully: {output_path}")
        
        # Verify file was downloaded
        if os.path.getsize(output_path) == 0:
            print("✗ Error: Downloaded file is empty!")
            os.remove(output_path)
            return False
        
        return True
        
    except requests.exceptions.Timeout:
        print("✗ Download timed out. Try again or use a faster connection.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Download failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Error downloading from Google Drive: {e}")
        return False


def ensure_model_exists(models_dir, google_drive_file_id=None):
    """
    Ensure model file exists. Download from Google Drive if needed.
    
    Args:
        models_dir: Path to models directory
        google_drive_file_id: Google Drive file ID (optional)
    
    Returns:
        Path to model file if exists, None otherwise
    """
    model_file = os.path.join(models_dir, 'trained_models.joblib')
    
    # If model already exists, return path
    if os.path.exists(model_file):
        file_size_mb = os.path.getsize(model_file) / (1024 * 1024)
        print(f"✓ Model found locally: {model_file} ({file_size_mb:.1f}MB)")
        return model_file
    
    # Try to download from Google Drive if file ID is provided
    if google_drive_file_id:
        print("Model not found locally. Attempting to download from Google Drive...")
        if download_from_google_drive(google_drive_file_id, model_file):
            return model_file
        else:
            print("Failed to download from Google Drive")
            return None
    
    print(f"Model file not found at: {model_file}")
    return None
