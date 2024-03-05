import whisper

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("base")
result = model.transcribe("audio.wav")
print(result["text"])