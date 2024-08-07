import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import tempfile
import pyttsx3
import google.generativeai as genai
from dotenv import load_dotenv
import os
from pathlib import Path
import streamlit as st

# Load environment variables from a .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def get_gemini_response(audio_data):
    """
    Generates a transcript from the audio data.

    Args:
        audio_data (bytes): The audio file data in bytes.

    Returns:
        str: The generated transcript from the AI model.
    """
    prompt = "Generate a transcript of the speech."
    response = model.generate_content([prompt, audio_data[0]]) 
    return response.text

def process_audio_file(uploaded_file):
    """
    Processes the uploaded audio file and returns its details.

    Args:
        uploaded_file (UploadedFile): The file uploaded by the user.

    Returns:
        bytes: The audio file data in bytes.

    Raises:
        FileNotFoundError: If no file is uploaded.
    """
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        audio_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return audio_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Initialize Streamlit App
st.set_page_config(page_title="Audio to Transcript")
st.header("Gemini Audio Transcription")

# File uploader for the audio file
uploaded_file = st.file_uploader("Choose an audio file...", type=['mp3', 'wav'])

# Submit button
submit = st.button("Transcribe Audio")

# If the Submit button is clicked
if submit:
    try:
        audio_data = process_audio_file(uploaded_file)
        response = get_gemini_response(audio_data)
        st.subheader("The Transcript is: ")
        st.write(response)
    except FileNotFoundError as e:
        st.error(e)
