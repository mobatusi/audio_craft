# AudioCraft Music Generator 🎵

Generate original music compositions using Meta AI's AudioCraft framework. This project provides both a Jupyter notebook for experimentation and a user-friendly Streamlit web application for interactive music generation.

## Technologies
- Python 3.x
- Meta AI AudioCraft
- PyTorch
- Streamlit
- TorchAudio

## Skills
- Machine Learning
- AI Frameworks
- Prompt Engineering
- Web Application Development

## Project Structure
```
audio_craft/
├── app.py                 # Streamlit web application
├── solution.ipynb         # Jupyter notebook with experiments
├── requirements.txt       # Python dependencies
└── README.md
```

## Features
- 🎼 **Interactive Web Interface**: User-friendly Streamlit app with real-time music generation
- 🎵 **Genre Presets**: Pre-defined prompts for Afrobeats, Electronic, Classical, Jazz, and Rock
- ✏️ **Custom Prompts**: Create your own music descriptions for personalized compositions
- 🔊 **Audio Playback**: Listen to generated music directly in the browser
- 💾 **Session Memory**: Keeps track of your last generated composition
- ⚡ **Model Caching**: Efficient model loading with Streamlit's caching system
- 🛠️ **Error Handling**: Robust error handling and user feedback

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/mobatusi/audio_craft
cd audio_craft
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install ffmpeg:
```bash
conda install "ffmpeg<5" -c conda-forge
```

## Usage

### Option 1: Streamlit Web App (Recommended)
Launch the interactive web application:
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` to access the music generator interface.

**Features:**
- Select from 5 music genres with pre-defined prompts
- Create custom music descriptions
- Generate 8-second audio clips
- Play generated music directly in your browser

### Option 2: Jupyter Notebook
For experimentation and learning:
```bash
jupyter notebook solution.ipynb
```

## Example Prompts
- **Afrobeats**: "upbeat afrobeats song with guitar solo"
- **Electronic**: "ambient electronic music with synthesizers" 
- **Classical**: "peaceful piano melody"
- **Jazz**: "smooth jazz with saxophone"
- **Rock**: "energetic rock song with guitar riffs"

## Tips for Better Results
- Be specific about instruments (guitar, piano, drums, saxophone)
- Mention the mood (upbeat, chill, energetic, peaceful)
- Include genre information (jazz, rock, electronic, classical)
- Describe tempo (fast, slow, moderate)

## Troubleshooting

### macOS Users
If you see AVFoundation warnings, they can be safely ignored. To suppress them:
```bash
PYTHONWARNINGS=ignore streamlit run app.py
```

### Memory Issues
The model requires significant memory. If you encounter issues:
- Close other applications
- Use the 'small' model variant (already configured)
- Restart the application if needed


## References
- [Generating New Music with Artificial Intelligence](https://www.educative.io/projects/generating-new-music-with-artificial-intelligence)
- [AudioCraft’s GitHub repository](https://github.com/facebookresearch/audiocraft)
- [TorchAudio](https://pytorch.org/audio/stable/index.html)