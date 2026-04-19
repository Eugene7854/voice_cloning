# Voice Clone Project

A simple voice cloning application that uses text-to-speech technology to generate audio in a cloned voice from a reference audio sample.

## Project Structure

```
voice_clone_1/
|-- voice_clone.py          # Main script for voice cloning
|-- my_voice_sample.wav     # Reference audio sample for voice cloning
|-- Outputs/                # Generated audio outputs
|   |-- output1.wav
|   |-- output2.wav
|   |-- ...
|-- test voice/             # Additional test voice samples
|   |-- my_voice_sample.wav
|-- requirements.txt        # Python dependencies
|-- README.md               # This file
```

## Features

- **Voice Cloning**: Clone a voice from a reference audio sample
- **Auto-incrementing Output**: Each generated audio is saved with an incremental filename (output1.wav, output2.wav, etc.)
- **Easy to Use**: Simple script with minimal configuration

## Prerequisites

- Python 3.8 or higher
- A reference audio sample (WAV format) for voice cloning
- Hugging Face account (required for model access)

## Hugging Face Authentication

This project uses models hosted on Hugging Face, which requires authentication. Follow these steps to set up:

### 1. Create a Hugging Face Account

1. Visit [https://huggingface.co](https://huggingface.co)
2. Click "Sign Up" to create a free account
3. Verify your email address

### 2. Generate an Access Token

1. Log in to your Hugging Face account
2. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Click "New token"
4. Give your token a name (e.g., "voice-clone")
5. Select token type: "Read" (recommended) or "Write" if needed
6. Click "Generate token"
7. **Important**: Copy the generated token immediately (you won't see it again)

### 3. Login via Command Line

After installing dependencies, authenticate with Hugging Face:

```bash
huggingface-cli login
```

When prompted, paste your access token and press Enter.

Alternatively, you can use the token directly in your code (not recommended for production):

```python
from huggingface_hub import login
login(token="your_access_token_here")
```

### 4. Accept Model Terms (if required)

Some models on Hugging Face require you to accept their terms of use:

1. Visit the model page (e.g., [https://huggingface.co/collections](https://huggingface.co/collections))
2. Click on the model being used by pocket-tts
3. Read and accept the license agreement if prompted
4. You may need to be logged in for this step

## Installation

1. Clone or download this repository

2. Create a virtual environment (recommended):
   ```bash
   python -m venv voiceClone
   voiceClone\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Login to Hugging Face:
   ```bash
   huggingface-cli login
   ```
   Paste your access token when prompted (see Hugging Face Authentication section above for details)

## Usage

1. Place your reference voice sample as `my_voice_sample.wav` in the project root (or update the path in the script)

2. Run the script:
   ```bash
   python voice_clone.py
   ```

   OR 
   ```
   python .\voice_clone.py
   ```

3. Generated audio will be saved in the `Outputs/` directory with incremental naming

## Customization

- **Change the text**: Modify the text in `voice_clone.py` line 13 to generate different audio
- **Change the voice sample**: Replace `my_voice_sample.wav` with your own reference audio or update the path in the script

## Dependencies

- `pocket-tts` - Text-to-speech library with voice cloning capabilities
- `scipy` - For audio file I/O operations
- `huggingface_hub` - For Hugging Face model authentication and access

## Notes

- The `voiceClone/` directory contains the virtual environment and should not be committed to version control
- Ensure your reference audio sample is clear and of good quality for best results
- **Hugging Face authentication is required** - you must login with `huggingface-cli login` before running the script
- If you encounter authentication errors, verify your token is valid and you've accepted any required model terms
