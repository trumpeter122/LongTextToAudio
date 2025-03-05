# Long Text to Audio

## Introduction

A Python program for generating audio from long text using [Kokoro](#kokoro) and [ffmpeg](#ffmpeg).

Instead of generating separate audio files for sentences or segments of a text (due to the limit of TTS models), it produces only one .wav file as the output, producing a more coherent experience for long text-to speech conversion.

## Features

1. Split a given text into sentences.

2. Use [Kokoro](#kokoro) to generate a `.wav` audio file for each sentence.

3. Use [ffmpeg](#ffmpeg) to merge the .wav files.

You can download and play the sample audios in the repo.

## Requirements
* Python 3.10.12
* [ffmpeg](#ffmpeg)

## Usage

1. Install [ffmpeg](#ffmpeg) with `sudo apt-get install ffmpeg`
1. Install the Python packages with `pip install -r requirements.txt`
1. Open main.ipynb
1. Run the cells

Feel free to modify the codes for your specific need.

## Acknowledgements

### Kokoro

* Hugging Face: https://huggingface.co/hexgrad/Kokoro-82M
* GitHub: https://github.com/hexgrad/kokoro/tree/main

### ffmpeg
* Official Website: https://ffmpeg.org/
* Github: https://github.com/FFmpeg/FFmpeg
