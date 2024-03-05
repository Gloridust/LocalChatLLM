import pyttsx3
import time

def tts(output_text):
    pyttsx3.speak(output_text)
    # time.sleep(5)

tts("Hello")