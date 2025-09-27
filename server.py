"""
Flask server for the Emotion Detector Application.
Provides endpoints to analyze emotions from text input.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the homepage with the input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Analyze the input text and return emotions with dominant emotion.
    If no valid text is given, return an error message.
    """
    text_to_analyze = request.form.get("textToAnalyze", "").strip()

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
