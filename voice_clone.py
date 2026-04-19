from pocket_tts import TTSModel
import scipy.io.wavfile
import os
import glob

# Load the model once
tts_model = TTSModel.load_model()
# Get voice state from reference audio
voice_state = tts_model.get_state_for_audio_prompt(
    "my_voice_sample.wav"
)
# Generate audio
audio = tts_model.generate_audio(voice_state, "Explore the marvels of the universe and unravel the mysteries of science. From the vastness of space to the intricacies of the human body, we'll embark on a voyage of discovery. Join us as we dive into groundbreaking research and awe-inspiring phenomena that shape our understanding of the world.")

# Find the next available output number
output_dir = "Outputs"
os.makedirs(output_dir, exist_ok=True)
existing_files = glob.glob(os.path.join(output_dir, "output*.wav"))
if existing_files:
    # Extract numbers from existing files and find the max
    numbers = []
    for f in existing_files:
        basename = os.path.basename(f)
        num = ''.join(filter(str.isdigit, basename.replace("output", "").replace(".wav", "")))
        if num:
            numbers.append(int(num))
    next_num = max(numbers) + 1 if numbers else 1
else:
    next_num = 1

# Save to file with incremented number
output_path = os.path.join(output_dir, f"output{next_num}.wav")
scipy.io.wavfile.write(output_path, tts_model.sample_rate, audio.numpy())
print(f"Saved to {output_path}")