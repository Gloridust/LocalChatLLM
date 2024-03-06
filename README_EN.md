# LocalChatLLM

LocalChatLLM is an open-source project led by the **YGeeker Pioneer** program, aimed at achieving out-of-the-box localized offline natural language voice interaction.

<a href="https://www.ygeeker.com">
  <img width="180" alt="Sponsored by YGeeker" src="https://www.ygeeker.com/badge/sponsor.png">
</a >

It's worth noting that this project supports bilingual capabilities in Chinese and English. Different language versions utilize different models: 'qwen:7b' for Chinese and 'gemma:7b' for English. Please choose the model according to your needs. [点击这里查看中文版本](./README.md).

## Main Technology Stack

- [x] Python  
- [x] Ollama  
- [x] Gemma
- [x] OpenAI-Whisper  
- [x] Pyttsx3  

## Features Implemented

- [x] LLM Natural Language Dialogue - Ollama|Qwen  
- [x] Voice Input - Whisper  
- [x] Speech Synthesis - Pyttsx3
- [ ] Implementation of Large Models for Natural Language Synthesis
- [ ] Voice Activation
- [ ] Automatic Termination of Recording
- [ ] Distributed Execution

## Changelog

### v1.1.0
- Added runtime detection feature, which can calculate the processing time of each loop:

```
asr time: 2.155439000001934 # Time for speech-to-text conversion
get_response time: 4.139052400001674 # Time for processing with large language model
all time: 6.295364899997367 # Total processing time
```

### v1.0.1

- Added text detection to automatically terminate the program if no one speaks.

### v1.0.0

- Implemented basic natural language voice interaction functionality.

## Deployment

1. Clone this repository:

```bash
git clone https://github.com/Gloridust/LocalChatLLM.git
cd ./LocalChatLLM
```

2. Install [Ollama](https://ollama.com/download) from its official website.

3. Install Python dependencies:

```python
pip install -r requirements.txt
```

If any exceptions occur, try installing step by step to identify where the problem lies:

```python
pip install ollama
pip install pyaudio
pip install pydub
pip install ffmpeg
pip install pyttsx3
pip install openai-whisper
```

Refer to the official documentation of [Openai-Whisper](https://github.com/openai/whisper?tab=readme-ov-file#setup) for ffmpeg installation commands based on different systems:

```shell
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

If you encounter installation errors in the 'pip install' commands mentioned above, you may need to install the Rust development environment. Additionally, you might need to configure the PATH environment variable, such as 'export PATH="$HOME/.cargo/bin:$PATH"'. If the module named "setuptools_rust" is not found and installation fails, you need to install 'setuptools_rust' first:

```bash
pip install setuptools-rust
```

4. Pull the required ollama model and customize:

```bash
ollama pull gemma:7b
ollama create localchatllm-gemma-7b -f ./modelfile_en
```

5. Initialize and try running whisper:

```bash
whisper audio.wav --language English --model small
```

You're all set!

## Running

```bash
python ./start.py
```

The program records for 5 seconds and then waits to generate a response. After reading out the generated response, it will enter the recording state again, looping through this process.

## Acknowledgments

- [YGeeker](https://github.com/ygeeker)
- [OpenAI-Whisper](https://github.com/openai/whisper)
- [Ollama](https://github.com/ollama/ollama-python)
- [Qwen](https://huggingface.co/Qwen)
- [Gemma](https://huggingface.co/Qwen)