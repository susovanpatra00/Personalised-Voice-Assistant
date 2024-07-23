import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import pyttsx3
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
import pathlib
import tempfile

# Load environment variables from a .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model
model = genai.GenerativeModel('models/gemini-1.5-flash')

def transcribe_audio(file_path):
    """
    Transcribes the audio file to text using the Gemini model.

    Args:
        file_path (str): The file path of the audio file.

    Returns:
        str: The generated transcript from the AI model.
    """
    prompt = """
                1. Generate a summary of the transcript of the speech. 
                2. Give Response to the transcript like a question answer chatbot within 500-1000 words.
                
                Example - 
                        Transcript- What is Generative AI?
                        Response- All details about the given transcript.
            """
    audio_data = pathlib.Path(file_path).read_bytes()

    response = model.generate_content([
        prompt,
        {
            "mime_type": "audio/wav",
            "data": audio_data
        }
    ])
    return response.text


def record_audio(duration, sample_rate=44100):
    """
    Records audio for a given duration.

    Args:
        duration (int): The duration of the recording in seconds.
        sample_rate (int): The sample rate for the recording.

    Returns:
        str: The file path of the recorded audio file.
    """
    try:
        st.write("Recording...")
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until the recording is finished

        # Save the recording to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        write(temp_file.name, sample_rate, recording)
        temp_file.close()
        return temp_file.name
    except Exception as e:
        st.error(f"An error occurred while recording audio: {e}")
        return None

# Initialize Streamlit App
st.set_page_config(page_title="Audio to Transcript and Answer")
st.header("Gemini Audio Question Answering")

# Button to start recording
if st.button("Start Recording"):
    audio_file_path = record_audio(5)
    if audio_file_path:
        st.write(f"Recording saved to {audio_file_path}")

        # Transcribe the audio from the saved file
        transcript = transcribe_audio(audio_file_path)
        st.write(transcript)

