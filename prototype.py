import pyaudio
import wave
from pydub import AudioSegment
import assemblyai as aai
from google import genai
import pyttsx3
import os

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


#STT with AssemblyAI API
aai.settings.api_key = os.environ["ASSEMBLYAI_API_KEY"]

# audio_file = "./local_file.mp3"
audio_file = "./recording.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)
transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print("Transcribe results:", transcript.text)


#LLM with Gemini API
content_qna = transcript.text

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-pro" ,
    contents=content_qna
)

print("Gemini Response :", response.text)


#TTS with pyttsx3
engine = pyttsx3.init()                      
engine.setProperty('rate', 140)     
                      
engine.setProperty('volume',1.0)        
engine.setProperty('voice', engine.getProperty('voices')[1].id)

engine.say(response.text)
engine.runAndWait()
engine.stop()

