"""
This module provides a Flask web application for detecting emotions in text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyzes the emotion of the provided text and returns the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is not None:
        output = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
        return output

    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
