import ollama
import whisper
import pyaudio
import wave
import os
import pyttsx3
import ssl
import sys
import time
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

######config#####

# For Chinese use 'qwen:7b'
model_name = 'qwen/Qwen-14B-Chat' 

# For English use 'gemma:7b'
# model_name = 'localchatllm-gemma-7b' 

whisper_model = "small"
whisper_language = "zh"
#################

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True).eval()
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

def record_audio(filename, duration=5, sample_rate=44100, chunk_size=1024, format=pyaudio.paInt16, channels=1):
    audio = pyaudio.PyAudio()
    # open microphone
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording...")

    frames = []
    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Recording finished.")

    # close microphone
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save audio
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print("Audio saved as", filename)


def asr(file):
    model = whisper.load_model(whisper_model)
    result = model.transcribe(file, language=whisper_language)
    print(result["text"])
    return(result["text"])

def delete_file(filename):
    try:
        os.remove(filename)
        print("File", filename, "deleted successfully.")
    except FileNotFoundError:
        print("File", filename, "not found.")

def tts(output_text):
    pyttsx3.speak(output_text)

def main_loop():
    # Record voice
    record_audio("audio.wav", duration=5)
    start_all = time.perf_counter()

    # ASR
    start_asr = time.perf_counter()
    user_input_text = asr("audio.wav")
    end_asr = time.perf_counter()

    # No voice input
    if user_input_text == "" or user_input_text == " you":
        print("no voice found")
        sys.exit(0)

    # Run LLM
    start_get_response = time.perf_counter()
    response, history = model.chat(tokenizer,user_input_text, history=history)
    print(history)
    end_get_response = time.perf_counter()
    
    print(response)
    end_all = time.perf_counter()

    print("asr time:",end_asr - start_asr)
    print("get_response time:",end_get_response - start_get_response)
    print("all time:",end_all - start_all)

    tts(response)

    # Delet File
    delete_file("audio.wav")
    message = {'role': 'user', 'content': user_input_text}

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    # os.system("ollama serve")

    while True:
        main_loop()
