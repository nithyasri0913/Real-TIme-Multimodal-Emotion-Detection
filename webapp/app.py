#
#   Main driver code for the Flask based web app on a localhost
#   created by Ronja Rehm and Jan Kühlborn
#
###################################################################################

from flask import Flask, render_template, Response, make_response, send_file
import audio_recognizer
import audio_recognizer8
import json
import video_recognizer
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

app = Flask(__name__, static_folder='static')
global audio_emotion
global audio_emotion_8
global multi_emotion


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_recognizer.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/audio')
def audio():
    return render_template('audio.html')


@app.route('/audio8')
def audio8():
    return render_template('audio_8emotions.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/multimodal')
def multimodal():
    return render_template('multimodal.html')


@app.route('/live-data')
def live_data():
    """ echo audio predictions as JSON"""
    global audio_emotion
    data = audio_recognizer.analyze_audio()
    audio_emotion = data
    response = make_response(json.dumps(data.tolist()))
    response.content_type = 'application/json'
    return response

@app.route('/live-data8')
def live_data8():
    """ echo audio predictions as JSON for 8 emotions"""
    global audio_emotion_8
    data = audio_recognizer8.analyze_audio()
    audio_emotion_8 = data
    response = make_response(json.dumps(data.tolist()))
    response.content_type = 'application/json'
    return response


@app.route('/live-data_video')
def live_data_video():
    """ echo video predictions as JSON"""
    f = open('video_prediction.json')
    data = json.load(f)
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


@app.route('/live-data_multi')
def live_data_multi():
    """ This function is called from graph_multi.js that updates the multimodal diagram.
    It fetches predictions, updates global variables and returns a multimodal prediction. """
    global multi_emotion
    f = open('video_prediction.json')
    video_data = json.load(f)
    audio_data = audio_recognizer.analyze_audio()
    newdict = [{"name": "Video",
                "data": [{"name": "Angry", "value": round(video_data[0] * 100, 2)},
                         {"name": "Fearful", "value": round(video_data[1] * 100, 2)},
                         {"name": "Happy", "value": round(video_data[2] * 100, 2)},
                         {"name": "Sad", "value": round(video_data[3] * 100, 2)}]},
               {"name": "Audio",
                "data": [{"name": "Angry", "value": round(audio_data[0] * 100, 2)},
                         {"name": "Fearful", "value": round(audio_data[1] * 100, 2)},
                         {"name": "Happy", "value": round(audio_data[2] * 100, 2)},
                         {"name": "Sad", "value": round(audio_data[3] * 100, 2)}]}]
    multimodal_data = []
    video_data = np.array(video_data)
    for i in range(len(audio_data)):
        multimodal_data.append(0.7 * video_data[i] + 0.3 * audio_data[i])
    multi_emotion = multimodal_data

    response = make_response(json.dumps(newdict))
    response.content_type = 'application/json'
    return response


@app.route('/spectrogram')
def spectrogram():
    """ returns diagrams that are updated by audio_recognizer.py"""
    return send_file('diagrams\\MelSpec.png', mimetype='image/png')


@app.route('/waveplot')
def waveplot():
    """ returns diagrams that are updated by audio_recognizer.py"""
    return send_file('diagrams\\Waveplot.png', mimetype='image/png')


@app.route('/emotion')
def emotion():
    """ returns emotion picture based on predictions """
    try:
        data = audio_emotion
    except NameError:   # catches events while starting when no data exists yet
        data = [0.0, 0.0, 0.0, 0.0]
    print('audio array: ', data)
    if np.argmax(data) == 0:
        return send_file('static\\images\\angry.png', mimetype='image/png')
    elif np.argmax(data) == 1:
        return send_file('static\\images\\fear.png', mimetype='image/png')
    elif np.argmax(data) == 2:
        return send_file('static\\images\\happy.png', mimetype='image/png')
    elif np.argmax(data) == 3:
        return send_file('static\\images\\sad.png', mimetype='image/png')
    else:
        return send_file('static\\images\\blank.png', mimetype='image/png')


@app.route('/emotion8')
def emotion8():
    try:
        data = audio_emotion_8
    except NameError:
        data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    print('audio array: ', data)
    if np.argmax(data) == 0:
        return send_file('static\\images\\angry.png', mimetype='image/png')
    elif np.argmax(data) == 3:
        return send_file('static\\images\\fear.png', mimetype='image/png')
    elif np.argmax(data) == 4:
        return send_file('static\\images\\happy.png', mimetype='image/png')
    elif np.argmax(data) == 6:
        return send_file('static\\images\\sad.png', mimetype='image/png')
    elif np.argmax(data) == 1:
        return send_file('static\\images\\calm.png', mimetype='image/png')
    elif np.argmax(data) == 2:
        return send_file('static\\images\\disgust.png', mimetype='image/png')
    elif np.argmax(data) == 5:
        return send_file('static\\images\\neutral.png', mimetype='image/png')
    elif np.argmax(data) == 7:
        return send_file('static\\images\\surprise.png', mimetype='image/png')
    else:
        return send_file('static\\images\\blank.png', mimetype='image/png')


@app.route('/multi_emotion')
def multi_emotion():
    try:
        data = multi_emotion
    except NameError:
        data = [0.0, 0.0, 0.0, 0.0]
    print('multi array: ', data)
    if np.argmax(data) == 0:
        return send_file('static\\images\\angry.png', mimetype='image/png')
    elif np.argmax(data) == 1:
        return send_file('static\\images\\fear.png', mimetype='image/png')
    elif np.argmax(data) == 2:
        return send_file('static\\images\\happy.png', mimetype='image/png')
    elif np.argmax(data) == 3:
        return send_file('static\\images\\sad.png', mimetype='image/png')
    else:
        return send_file('static\\images\\blank.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=False)
