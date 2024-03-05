import ollama
import whisper
import pyaudio
import wave
import os

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def record_audio(filename, duration=5, sample_rate=44100, chunk_size=1024, format=pyaudio.paInt16, channels=1):
    audio = pyaudio.PyAudio()
    # 打开麦克风
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

    # 关闭麦克风
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 保存录制的音频文件
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print("Audio saved as", filename)


def asr():
    model = whisper.load_model("base")
    result = model.transcribe("audio.wav")
    print(result["text"])
    return(result["text"])

def get_response(message):
    model_name = 'qwen:14b'
    response = ollama.chat(
        model=model_name, 
        messages=message,
        stream=False,
    )
    output_text = response['message']['content']
    received_message = response['message']
    return output_text, received_message

def delete_file(filename):
    try:
        os.remove(filename)
        print("File", filename, "deleted successfully.")
    except FileNotFoundError:
        print("File", filename, "not found.")

if __name__ == "__main__":
    message_history = []
    while True:
        record_audio("audio.wav", duration=5)
        # user_input_text = input("Input:")
        user_input_text = asr()
        message = {'role': 'user', 'content': user_input_text}
        message_history.append(message)
        output_text, received_message = get_response(message_history)
        message_history.append(received_message)
        print(output_text)
        delete_file("audio.wav")
        # print(message_history)
