from openai import OpenAI
import os

cdir_path = os.getcwd()
mp3_path=os.path.join(cdir_path,"recording.mp3")

client = OpenAI()
audio_file = open(mp3_path,"rb")

transcript= client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print(transcript.text)