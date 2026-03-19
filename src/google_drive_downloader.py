"""
Google Drive Model Downloader
Downloads pre-trained models from Google Drive using gdown
"""

import os
from pathlib import Path

def download_from_google_drive(file_id, output_path):
    """
    Download a file from Google Drive using gdown
    
    Args:
        file_id: Google Drive file ID (from shareable link)
        output_path: Local path to save the file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        import gdown
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Google Drive URL
        url = f"https://drive.google.com/uc?id={file_id}"
        
        print(f"Downloading model from Google Drive using gdown...")
        print(f"File ID: {file_id}")
        print(f"Destination: {output_path}")
        
        # Download with gdown (more reliable for Google Drive)
        output = gdown.download(url, output_path, quiet=False)
        
        # Verify file was downloaded
        if not os.path.exists(output_path):
            print("✗ Error: File was not downloaded")
            return False
        
        file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
        
        if file_size_mb == 0:
            print("✗ Error: Downloaded file is empty (0 bytes)!")
            os.remove(output_path)
            return False
        
        print(f"✓ Model downloaded successfully: {output_path} ({file_size_mb:.1f}MB)")
        return True
        
    except ImportError:
        print("✗ gdown not installed. Install with: pip install gdown")
        return False
    except Exception as e:
        print(f"✗ Error downloading from Google Drive: {e}")
        import traceback
        traceback.print_exc()
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
        
        # Check if file is actually valid (not too small)
        if file_size_mb > 10:  # Should be at least ~3.9GB
            print(f"✓ Model found locally: {model_file} ({file_size_mb:.1f}MB)")
            return model_file
        else:
            print(f"⚠ Found file but it seems incomplete ({file_size_mb:.1f}MB). Re-downloading...")
            os.remove(model_file)
    
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
