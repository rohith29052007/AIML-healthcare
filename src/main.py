"""
Main Entry Point for AI Healthcare Assistant
Launches the GUI application
"""

import sys
import os
from pathlib import Path

# Add src directory to path
src_path = os.path.join(os.path.dirname(__file__))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from gui_app import main


if __name__ == "__main__":
    # Check if models are trained
    # Go up one level from src to project root
    project_root = Path(__file__).parent.parent
    models_path = os.path.join(project_root, "models", "trained_models.joblib")
    
    if not os.path.exists(models_path):
        print("="*60)
        print("ERROR: Models not found!")
        print("="*60)
        print("\nPlease train the models first by running:")
        print("  python src/train_model.py")
        print("\nThen launch the application with:")
        print("  python src/main.py")
        print("="*60)
        sys.exit(1)
    
    print("="*60)
    print("Launching AI Healthcare Assistant...")
    print("="*60)
    
    # Launch GUI
    main()
