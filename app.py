import streamlit as st
import torch
import torchaudio
from audiocraft.models import MusicGen
import numpy as np
import warnings
import os
import sys

# Suppress all warnings
warnings.filterwarnings("ignore")
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

# Suppress macOS AVFoundation warnings
if sys.platform == "darwin":
    os.environ['PYTHONWARNINGS'] = 'ignore'
    import logging
    logging.getLogger().setLevel(logging.ERROR)

st.set_page_config(
    page_title="AudioCraft Music Generator",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_model():
    """Load the MusicGen model and cache it for reuse"""
    try:
        with st.spinner("Loading MusicGen model... This may take a moment."):
            model = MusicGen.get_pretrained('facebook/musicgen-small')
            model.set_generation_params(duration=8)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def generate_music(model, prompt):
    """Generate music from text prompt"""
    if model is None:
        st.error("Model not loaded properly. Please refresh the page.")
        return None, None
        
    try:
        with st.spinner(f"Generating music for: '{prompt}'"):
            # Clear CUDA cache if using GPU
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            audio_samples = model.generate([prompt])
            sampling_rate = model.sample_rate
            audio_np = audio_samples[0].cpu().numpy()
            
            # Ensure audio is in the right format
            if audio_np.ndim > 1:
                audio_np = audio_np.squeeze()
                
        return audio_np, sampling_rate
    except Exception as e:
        st.error(f"Error generating music: {str(e)}")
        return None, None

def main():
    st.title("🎵 AudioCraft Music Generator")
    st.markdown("Generate original music compositions using Meta AI's AudioCraft framework")
    
    # Sidebar for predefined prompts
    with st.sidebar:
        st.header("🎼 Genre Presets")
        st.markdown("Choose from predefined prompts or create your own!")
        
        # Genre categories with predefined prompts
        genres = {
            "Afrobeats": [
                "upbeat afrobeats song with guitar solo",
                "energetic afrobeats song with heavy drums",
                "melodic afrobeats ballad with piano",
                "afrobeats song with bass guitar riff",
                "chill afrobeats with electric guitar and drums"
            ],
            "Electronic": [
                "ambient electronic music with synthesizers",
                "upbeat techno beat with bass drops",
                "dreamy synth-pop melody",
                "energetic EDM track with heavy bass"
            ],
            "Classical": [
                "peaceful piano melody",
                "orchestral symphony with strings",
                "classical guitar piece",
                "baroque style composition"
            ],
            "Jazz": [
                "smooth jazz with saxophone",
                "upbeat jazz with piano and drums",
                "jazz fusion with electric guitar",
                "mellow jazz ballad"
            ],
            "Rock": [
                "energetic rock song with guitar riffs",
                "heavy metal with drums and bass",
                "acoustic rock ballad",
                "indie rock with catchy melody"
            ]
        }
        
        selected_genre = st.selectbox("Select Genre:", list(genres.keys()))
        selected_prompt = st.selectbox("Choose Preset:", genres[selected_genre])
        
        if st.button("Use This Preset", type="secondary"):
            st.session_state.current_prompt = selected_prompt
            st.rerun()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("✍️ Music Prompt")
        
        # Initialize session state for current prompt
        if 'current_prompt' not in st.session_state:
            st.session_state.current_prompt = "upbeat afrobeats song with guitar solo"
        
        # Text area for custom prompts
        user_prompt = st.text_area(
            "Enter your music description:",
            value=st.session_state.current_prompt,
            height=100,
            help="Describe the style, instruments, mood, and genre of music you want to generate"
        )
        
        # Generate button
        generate_clicked = st.button("🎵 Generate Music", type="primary", use_container_width=True)
        
        if generate_clicked and user_prompt.strip():
            # Load model
            model = load_model()
            
            if model is not None:
                # Generate music
                audio_data, sample_rate = generate_music(model, user_prompt.strip())
                
                if audio_data is not None:
                    st.success("Music generated successfully!")
                    
                    # Display audio player
                    st.audio(audio_data, sample_rate=sample_rate)
                    
                    # Store in session state
                    st.session_state.last_generated = {
                        'audio': audio_data,
                        'sample_rate': sample_rate,
                        'prompt': user_prompt.strip()
                    }
        
        elif generate_clicked:
            st.warning("Please enter a music description first!")
    
    with col2:
        st.header("ℹ️ Tips")
        st.markdown("""
        **For better results:**
        
        • Be specific about instruments (guitar, piano, drums)
        • Mention the mood (upbeat, chill, energetic)
        • Include genre information (jazz, rock, electronic)
        • Describe tempo (fast, slow, moderate)
        
        **Examples:**
        - "Chill jazz with piano and light drums"
        - "Energetic rock song with guitar solo"
        - "Ambient electronic music with synthesizers"
        """)
        
        # Display last generated info
        if 'last_generated' in st.session_state:
            st.header("🎼 Last Generated")
            st.write(f"**Prompt:** {st.session_state.last_generated['prompt']}")
            st.audio(
                st.session_state.last_generated['audio'], 
                sample_rate=st.session_state.last_generated['sample_rate']
            )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "Built with [AudioCraft](https://github.com/facebookresearch/audiocraft) by Meta AI | "
        "Powered by Streamlit"
    )

if __name__ == "__main__":
    main()