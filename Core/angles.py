class Angles:
    angle_names = [
        'elbowLeft',
        'elbowRight',
        'kneeLeft',
        'kneeRight',
        'shoulderLeft',
        'shoulderRight',
        'torso',
        'ankleLeft',
        'ankleRight',
        'hipLeft',
        'hipRight',
        'wristLeft',
        'wristRight',
        'neck',
        'stick'
    ]

    def __init__(self) -> None:
        self._angles = {}
        for name in self.angle_names:
            self._angles[name] = 0.0

    def getangle(self, angle_name: str) -> float:
        return self._angles[angle_name]
    
    def setangle(self, angle_name: str, angle: float) -> None:
        self._angles[angle_name] = angle