from flask import Flask
import flask
import cv2
from External.mediapipeposecalculator import MediaPipePoseCalculator
from Interface.anglecalculator import AngleCalculatorFromNPArray
import json
import numpy as np

app = Flask(__name__)
@app.route('/upload/file', methods=['POST'])
def upload():
    file_bytes = None
    try:
        imagefile = flask.request.files.get('imagefile', '')
        file_bytes = np.fromfile(imagefile, np.uint8)    
    except Exception as err:
        return 'Read error: ' + str(err)
    try:
        return process_frame(file_bytes)
    except Exception as err:
        return 'OpenCV error: ' + str(err)
    
@app.route('/upload/bytes', methods=['POST'])
def upload_bytes():
    image_bytes = bytes(flask.request.get_json()['imagebytes'])
    image_np = np.fromstring(image_bytes, np.uint8)
    return process_frame(image_np)

def process_frame(frame):
    data = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    posecalculator = MediaPipePoseCalculator()
    angles = AngleCalculatorFromNPArray(data, posecalculator).calculateangle()
    return json.dumps({
        'angles': angles.angles,
        'image': cv2.imencode('.jpg', angles.annotated_image)[1].tolist()
    })