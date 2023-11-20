from flask import Flask, render_template, Response, request
import flask
import cv2
import threading
from External.mediapipeposecalculator import MediaPipePoseCalculator
from Interface.anglecalculator import AngleCalculatorFromNPArray
import json
import numpy as np

app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload():
    file_bytes = None
    try:
        imagefile = flask.request.files.get('imagefile', '')
        file_bytes = np.fromfile(imagefile, np.uint8)    
    except Exception as err:
        return 'Read error: ' + str(err)
    try:
        data = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR) 
        cv2.imwrite('cv2.jpg', data)
        posecalculator = MediaPipePoseCalculator()
        angles = AngleCalculatorFromNPArray(data, posecalculator).calculateangle()
        print(angles)
        return json.dumps(angles)
    except Exception as err:
        return 'OpenCV error: ' + str(err)