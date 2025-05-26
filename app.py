import streamlit as st
from emotion_detector import detect_emotion

st.set_page_config(page_title="Real-Time Emotion to Emoji", page_icon="🎧")
st.title("🎧 Real-Time Emotion to Emoji")

st.markdown("""
Upload a 5-second **WAV** audio clip of your voice, and the AI will detect your emotion and show an emoji!
""")

uploaded_file = st.file_uploader("📤 Upload your 5-second WAV audio", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')

    with st.spinner("Detecting emotion..."):
        emotion, emoji = detect_emotion(uploaded_file)
        st.markdown(f"## {emoji} Emotion: **{emotion.title()}**")
