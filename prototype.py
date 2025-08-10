import pyaudio
import wave
import os
from pydub import AudioSegment

# Folder penyimpanan
save_dir = os.getcwd()
save_path = os.path.join(save_dir, "recording.wav")
mp3_path = os.path.join(save_dir, "recording.mp3")

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

print("Recording... Press CTRL+C to stop.")

try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    print("\nDone Record.")

stream.stop_stream()
stream.close()
audio.terminate()

# Simpan WAV
sound_file = wave.open(save_path, "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()

print(f"File WAV saved in: {save_path}")

# Konversi ke MP3
sound = AudioSegment.from_wav(save_path)
sound.export(mp3_path, format="mp3")

print(f"File MP3 saved in: {mp3_path}")

