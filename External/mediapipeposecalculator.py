from Interface.anglecalculator import PoseCalculatorFromNPArray
from Interface.anglecalculator import AngleCalculatorFromNPArray
from External.mediapipepose import getmediapipeposes
import cv2
import numpy as np 
from External.utils import poselandmarkerresult2dict
from Interface.anglecalculator import AngleOutput
from Interface.anglecalculator import PoseOutput

class MediaPipePoseCalculator(PoseCalculatorFromNPArray):

    def calculate33posefromnp(self, data: np.array):
         landmarks, annotated_image = getmediapipeposes(data)
         return PoseOutput(poselandmarkerresult2dict(landmarks), annotated_image)

'''data = cv2.imread('/Users/vk/dev/PoseEstimation/External/test_img.jpg', 1)
posecalculator = MediaPipePoseCalculator()
# posedict = poselandmarkerresult2dict(posecalculator.calculate33posefromnp(data))
print(AngleCalculatorFromNPArray(data, posecalculator).calculateangle())'''
