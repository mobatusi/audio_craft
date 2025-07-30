#!/usr/bin/env python3
"""
Test script to verify deployment dependencies
"""
import sys
import os

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import torch
        print(f"✅ PyTorch imported successfully (version: {torch.__version__})")
    except ImportError as e:
        print(f"❌ PyTorch import failed: {e}")
        return False
    
    try:
        import torchaudio
        print(f"✅ TorchAudio imported successfully (version: {torchaudio.__version__})")
    except ImportError as e:
        print(f"❌ TorchAudio import failed: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✅ NumPy imported successfully (version: {np.__version__})")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    try:
        from audiocraft.models import MusicGen
        print("✅ AudioCraft imported successfully")
    except ImportError as e:
        print(f"❌ AudioCraft import failed: {e}")
        return False
    
    try:
        import plotly
        print(f"✅ Plotly imported successfully (version: {plotly.__version__})")
    except ImportError as e:
        print(f"❌ Plotly import failed: {e}")
        return False
    
    try:
        import librosa
        print(f"✅ Librosa imported successfully (version: {librosa.__version__})")
    except ImportError as e:
        print(f"❌ Librosa import failed: {e}")
        return False
    
    return True

def test_model_loading():
    """Test if the model can be loaded"""
    print("\nTesting model loading...")
    
    try:
        from audiocraft.models import MusicGen
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        print("✅ Model loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def main():
    print("🚀 AudioCraft Deployment Test")
    print("=" * 40)
    
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test model loading
        model_ok = test_model_loading()
        
        if model_ok:
            print("\n🎉 All tests passed! Your deployment should work.")
        else:
            print("\n⚠️  Model loading failed. This might be due to memory constraints.")
    else:
        print("\n❌ Some imports failed. Check your requirements.txt")

if __name__ == "__main__":
    main() 