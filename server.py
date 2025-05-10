"""Module to run emotion detection Flask app on localhost."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detection():
    """
    Endpoint that performs emotion detection on the input text.

    Returns:
        str: Formatted string with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "¡Entrada no válida! Intenta de nuevo."

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!."

    # Formatea la respuesta como texto
    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result

@app.route("/")
def render_index_page():
    """
    Renders the main application page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Runs the Flask app on localhost at port 5001.
    app.run(host="0.0.0.0", port=5001)
