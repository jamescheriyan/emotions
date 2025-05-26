import streamlit as st
import sounddevice as sd
import scipy.io.wavfile as wav
from emotion_detector import detect_emotion
import os

st.set_page_config(page_title="Real-Time Emotion to Emoji", page_icon="🎧")
st.title(":headphones: Real-Time Emotion to Emoji")

st.markdown("""
Speak into your microphone for **5 seconds**, and this AI will detect your emotion and display an emoji!
""")

# Temporary file for recording
audio_path = "live.wav"

if st.button("🔊 Start Listening"):
    with st.spinner("Listening for 5 seconds..."):
        fs = 16000  # 16kHz sample rate
        duration = 5  # seconds
        recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        wav.write(audio_path, fs, recording)

    with st.spinner("Detecting emotion..."):
        emotion, emoji = detect_emotion(audio_path)
        st.markdown(f"## {emoji} Emotion: **{emotion.title()}**")

    # Clean up
    os.remove(audio_path)