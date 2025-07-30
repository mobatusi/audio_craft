#!/usr/bin/env python3
"""
Install AudioCraft with proper error handling for Streamlit Cloud
"""
import subprocess
import sys
import os

def install_audiocraft():
    """Install AudioCraft with fallback methods"""
    print("🔧 Installing AudioCraft...")
    
    # Method 1: Try direct installation
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "install", "audiocraft"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ AudioCraft installed successfully")
            return True
        else:
            print(f"❌ Direct installation failed: {result.stderr}")
    except Exception as e:
        print(f"❌ Error in direct installation: {e}")
    
    # Method 2: Try with specific version
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "install", "audiocraft==1.0.0"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ AudioCraft 1.0.0 installed successfully")
            return True
        else:
            print(f"❌ Version-specific installation failed: {result.stderr}")
    except Exception as e:
        print(f"❌ Error in version-specific installation: {e}")
    
    # Method 3: Try with --no-deps and manual dependency installation
    try:
        # Install dependencies manually first
        deps = ["av>=11.0.0", "einops>=0.8.0", "flashy>=0.0.1", "hydra-core>=1.1", 
                "hydra-colorlog>=1.2.0", "julius>=0.2.7", "num2words>=0.5.14", 
                "sentencepiece>=0.2.0"]
        
        for dep in deps:
            subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                         capture_output=True, text=True)
        
        # Try installing AudioCraft without dependencies
        result = subprocess.run([sys.executable, "-m", "pip", "install", "audiocraft", "--no-deps"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ AudioCraft installed without dependencies")
            return True
        else:
            print(f"❌ No-deps installation failed: {result.stderr}")
    except Exception as e:
        print(f"❌ Error in no-deps installation: {e}")
    
    print("❌ All AudioCraft installation methods failed")
    return False

if __name__ == "__main__":
    install_audiocraft() 