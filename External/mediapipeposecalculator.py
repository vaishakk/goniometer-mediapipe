from Interface.anglecalculator import PoseCalculatorFromNPArray
from Interface.anglecalculator import AngleCalculatorFromNPArray
from mediapipepose import getmediapipeposes
import cv2
import numpy as np 
from utils import poselandmarkerresult2dict

class MediaPipePoseCalculator(PoseCalculatorFromNPArray):

    def calculate33posefromnp(self, data: np.array):
         return poselandmarkerresult2dict(getmediapipeposes(data))

data = cv2.imread('/Users/vk/dev/PoseEstimation/External/test_img.jpg', 1)
posecalculator = MediaPipePoseCalculator()
# posedict = poselandmarkerresult2dict(posecalculator.calculate33posefromnp(data))
print(AngleCalculatorFromNPArray(data, posecalculator).calculateangle())
