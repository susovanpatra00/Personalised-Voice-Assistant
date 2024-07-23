# Personalized Voice Assistant Chatbot

This project consists of a personalized voice assistant chatbot that can transcribe audio files, summarize the transcripts, and provide responses to questions. It includes three code files:

1. **`readaudio.py`**: Upload an audio file to receive a summary of the transcript.
2. **`readaudio_response.py`**: Upload an audio file to get a summary of the transcript and a response to the transcript.
3. **`recordaudio_readaudio_response.py`**: Record audio directly, receive a summary of the transcript, and get a response.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `sounddevice` package
- `numpy` package
- `scipy` package
- `pyttsx3` package
- `google-generativeai` package
- `python-dotenv` package
- `streamlit` package

You can install the required packages using pip:

```bash
pip install sounddevice numpy scipy pyttsx3 google-generativeai python-dotenv streamlit
```

## Environment Variables

Create a `.env` file in the project directory and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Files

### `readaudio.py`

This script takes an audio file as input and provides a summary of the transcript.

### `readaudio_response.py`

This script takes an audio file as input, provides a summary of the transcript, and generates a response based on the transcript.

### `recordaudio_readaudio_response.py`

This script records audio directly, provides a summary of the transcript, and generates a response based on the transcript. It uses Streamlit for the user interface. Right now the duration of the recording is 
set to 5 seconds but you can change it as your wish.

## Usage

### Running `recordaudio_readaudio_response.py`

1. Run the script using Streamlit:

    ```bash
    streamlit run recordaudio_readaudio_response.py
    ```

2. Open the provided URL in your browser.
3. Click the "Start Recording" button to record audio.
4. The application will automatically transcribe the recorded audio, provide a summary of the transcript, and generate a response based on the transcript.

## Acknowledgements

- [Google Gemini](https://cloud.google.com/generative-ai) for the AI model.
- [Streamlit](https://streamlit.io) for the interactive web application framework.
- [Sounddevice](https://github.com/spatialaudio/python-sounddevice) for audio recording.
- [Scipy](https://www.scipy.org) for audio file handling.
```
