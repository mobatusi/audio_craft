import torch
import torchaudio
import audiocraft
from audiocraft.models import MusicGen
import numpy as np

def generate_music():
    # Load the small model for faster inference
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    
    # Set the duration of the generated music to 8 seconds
    model.set_generation_params(duration=8)
    
    # Define text prompts for different music styles
    prompts = ["Chill Afrobeats with electric guitar and drums", "catchy afrobeats song with upbeat melody"]
    
    try:
        # Generate the music samples
        audio_samples = model.generate(prompts)
        
        # Get the sampling rate from the model's configuration
        sampling_rate = model.sample_rate
        
        # Save the generated audio samples
        for i, audio in enumerate(audio_samples):
            # Convert to numpy array and save as WAV file
            audio_np = audio.cpu().numpy()
            torchaudio.save(f'generated_music_{i}.wav', torch.from_numpy(audio_np), sampling_rate)
            print(f"Saved generated music {i} as 'generated_music_{i}.wav'")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Numpy version:", np.__version__)
        print("Torch version:", torch.__version__)

if __name__ == "__main__":
    generate_music() 