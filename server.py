'''
server hosting
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")
@app.route("/emotionDetector")
def emotion_detect():
    '''
    Calls the emotion detector
    '''
    text = request.args.get('textToAnalyze')

    response = emotion_detector(text)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid Text! Please try again!"

    response_string = f"'anger': {response['anger']}, " \
        f"'disgust': {response['disgust']}, "\
        f"'fear': {response['fear']}, " \
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}"

    return f"For the given statement, the system response is {response_string}." \
        f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''
    Renders the index.html page
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
