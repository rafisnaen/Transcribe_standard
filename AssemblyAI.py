import assemblyai as aai
from google import genai
import pyttsx3

import os

aai.settings.api_key = os.environ["ASSEMBLYAI_API_KEY"]

# audio_file = "./local_file.mp3"
audio_file = "./recording.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print("Transcribe results:", transcript.text)

content_qna = transcript.text

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-pro" ,
    contents=content_qna
)

print("Gemini Response :", response.text)

engine = pyttsx3.init()                      
engine.setProperty('rate', 125)     
                      
engine.setProperty('volume',1.0)        
engine.setProperty('voice', engine.getProperty('voices')[1].id)

engine.say(response.text)
engine.runAndWait()
engine.stop()
