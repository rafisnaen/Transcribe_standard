import assemblyai as aai

aai.settings.api_key = "6044d6cc7c6243a4ac5333fdf294f800"

# audio_file = "./local_file.mp3"
audio_file = "./recording.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)