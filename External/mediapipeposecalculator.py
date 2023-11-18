from Interface.anglecalculator import PoseCalculatorFromNPArray
from Interface.anglecalculator import AngleCalculatorFromNPArray
from mediapipepose import getmediapipeposes
import cv2

class MediaPipePoseCalculator(PoseCalculatorFromNPArray):

    def calculate33posefromnp():
        data = cv2.imread('/Users/vk/dev/PoseEstimation/External/test_img.jpg', 1)
        print(getmediapipeposes(data).Landmarks)

calculator = MediaPipePoseCalculator()
calculator.calculate33posefromnp()