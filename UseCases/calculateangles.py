from Core.media import Media
from Core.poselandmarks import Image33LandMarks
from Core.landmark import Landmark
from Core.angles import Angles
from Core.utils import dotproduct, abs
import math

class AngleCalculator:
    angles = Angles()

    angletoposemap = {
        'elbowLeft' : ('left shoulder', 'left wrist', 'left elbow'),
        'elbowRight': ('right shoulder', 'right wrist', 'right elbow'),
        'kneeLeft': ('left hip', 'left ankle', 'left knee'),
        'kneeRight': ('left hip', 'left ankle', 'left knee'),
        'shoulderLeft': ('left hip', 'left elbow', 'left shoulder'),
        'shoulderRight': ('right hip', 'right elbow', 'right shoulder'),
        'torso': (),
        'ankleLeft': ('left knee', 'left foot index', 'left ankle'),
        'ankleRight': ('right knee', 'right foot index', 'right ankle'),
        'hipLeft': ('left shoulder', 'left knee', 'left hip'),
        'hipRight':('right shoulder', 'right knee', 'right hip'),
        'wristLeft': ('left elbow', 'left index', 'left wrist'),
        'wristRight': ('right elbow', 'right index', 'right wrist'),
        'neck': ()
    }

    def calculateangles(self, poses: Image33LandMarks) -> Angles:
        

        return 
    
    def calculateanglefrompoints(self, point1: tuple, point2: tuple, centrepoint: tuple) -> float:
        normalised_point1 = (point1[0] - centrepoint[0]), (point1[1] - centrepoint[1])
        normalised_point2 = (point2[0] - centrepoint[0]), (point2[1] - centrepoint[1])
        return math.acos(dotproduct(normalised_point1, normalised_point2) / (abs(normalised_point1) * abs(normalised_point2)))
    
    def calculateanglefromposes(self, anglename: str, landmarks: Image33LandMarks) -> float:
        requiredposes = self.angletoposemap[anglename]
        return self.calculateanglefrompoints(landmarks.getlandmark(requiredposes[0]).getposition(),
                                            landmarks.getlandmark(requiredposes[1]).getposition(),
                                            landmarks.getlandmark(requiredposes[2]).getposition())
