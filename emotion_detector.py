# emotion_detector.py
import torchaudio
from speechbrain.inference.classifiers import AudioClassifier

# Load pretrained model
classifier = AudioClassifier.from_hparams(
    source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",
    savedir="pretrained_models/emotion-recognition"
)

EMOTION_EMOJIS = {
    "angry": "😠",
    "happy": "😄",
    "neutral": "😐",
    "sad": "😢",
    "fearful": "😨"
}

def detect_emotion(audio_file):
    signal, fs = torchaudio.load(audio_file)
    prediction = classifier.classify_file(audio_file)
    emotion = prediction[3]  # This is the predicted label
    emoji = EMOTION_EMOJIS.get(emotion.lower(), "❓")
    return emotion, emoji
