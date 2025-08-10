from pydub import AudioSegment

sound = AudioSegment.from_wav("record.wav")
sound.export("record.mp3", format="mp3")

print(f"File MP3")