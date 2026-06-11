from Interface.anglecalculator import PoseCalculatorFromNPArray
from External.mediapipepose import getmediapipeposes
import numpy as np 
from External.utils import poselandmarkerresult2dict
from Interface.anglecalculator import PoseOutput

class MediaPipePoseCalculator(PoseCalculatorFromNPArray):

    def calculate33posefromnp(self, data: np.array):
         landmarks, annotated_image = getmediapipeposes(data)
         return PoseOutput(poselandmarkerresult2dict(landmarks), annotated_image)

