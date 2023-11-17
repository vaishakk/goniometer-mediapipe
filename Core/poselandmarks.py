from Core.landmark import Landmark
from Core.media import Media

class Image33LandMarks:

    landmark_names = [
        'nose', 
        'left eye (inner)', 
        'left eye', 
        'left eye (outer)', 
        'right eye (inner)', 
        'right eye', 
        'right eye (outer)',
        'left ear',
        'right ear',
        'mouth (left)',
        'mouth (right)',
        'left shoulder',
        'right shoulder',
        'left elbow',
        'right elbow',
        'left wrist',
        'right wrist',
        'left pinky',
        'right pinky',
        'left index',
        'right index',
        'left thumb',
        'right thumb',
        'left hip',
        'right hip',
        'left knee',
        'right knee',
        'left ankle',
        'right ankle',
        'left heel',
        'right heel',
        'left foot index',
        'right foot index'
        ]
    
    _landmarks = {}

    def getlandmarknames(self) -> list:
        return self.landmark_names

    def __init__(self, imagepath: str) -> None:
        self._image = Media('img', imagepath)
        for pose in self.landmark_names:
            self._landmarks[pose] = Landmark(name=pose)

    def getmedia(self) -> Media:
        return self._image

    def getlandmarks(self) -> list:
        return self._landmarks
    
    def getlandmark(self, pose: str) -> Landmark:
        return self._landmarks[pose]
    
    def setlandmarks(self, landmarks: list) -> None:
        self._landmarks = landmarks

    def setlandmark(self, pose: str, position: tuple) -> None:
        self._landmarks[pose].setposition(position)