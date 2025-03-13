import streamlit as st
from audio_recorder_streamlit import audio_recorder
import requests
import os
import tempfile

API_URL = "http://localhost:8000"

st.set_page_config(page_title="VBDMS", page_icon="🎙", layout="centered")
st.title("🎙 Voice-Based Database Management System")

st.markdown(
    """
    <style>
        .big-button {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            padding: 15px;
            font-size: 18px;
            font-weight: bold;
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            border: none;
            transition: 0.3s;
        }
        .big-button:hover {
            background-color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def transcribe_audio(audio_file_path):
    """
    Function to transcribe audio file - sends to API endpoint
    """
    with open(audio_file_path, "rb") as audio_file:
        files = {"audio_file": audio_file}
        response = requests.post(f"{API_URL}/transcribe_audio/", files=files)
        if response.status_code == 200:
            return response.json()["text"]
        else:
            st.error(f"Error transcribing audio: {response.text}")
            return None

def process_command(command):
    """
    Send command to API and get response
    """
    try:
        response = requests.post(f"{API_URL}/process_voice_command/", json={"command": command})
        if response.status_code == 200:
            return response.json()["message"]
        else:
            st.error(f"Error processing command: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Main app
st.write("### 🔊 Click the microphone button below and speak your command")
st.write("Try saying: 'What is the maximum value of sensor 1?' or 'What is the status of sensor 2?'")

# Audio recorder
audio_bytes = audio_recorder(
    text="🎤 Click to record",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_size="2x",
)

# Process when we have audio
if audio_bytes:
    st.success("🎵 Audio recorded! Processing...")
    
    # Save audio to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        tmp_file.write(audio_bytes)
        audio_file_path = tmp_file.name
    
    # Display the audio
    st.audio(audio_bytes, format="audio/wav")
    
    # Transcribe audio
    with st.spinner("Transcribing..."):
        transcribed_text = transcribe_audio(audio_file_path)
    
    # Clean up temporary file
    os.unlink(audio_file_path)
    
    # Display transcribed text and process command
    if transcribed_text:
        st.write("### 📝 Transcribed command:")
        st.info(transcribed_text)
        
        # Process the command
        with st.spinner("Processing command..."):
            response = process_command(transcribed_text)
        
        if response:
            st.write("### 🤖 Response:")
            st.success(response)

# Sidebar (optional for future features)
with st.sidebar:
    st.header("⚙ Settings")
    st.write("Voice commands you can try:")
    st.markdown("""
    - "What is the maximum value of sensor 1?"
    - "What is the minimum value of sensor 2?"
    - "What is the last value of sensor 3?"
    - "What is the status of sensor 4?"
    """)

st.toast("🎉 Ready to take your command!", icon="✅")