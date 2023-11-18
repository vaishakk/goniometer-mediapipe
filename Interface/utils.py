from Core.poselandmarks import Image33LandMarks
from Core.angles import Angles

def dict2landmarks(poses: dict) -> Image33LandMarks:
    landmarks = Image33LandMarks('')
    for landmark in landmarks.getlandmarknames():
        try:
            landmarks.setlandmark(landmark, poses[landmark])
        except:
            print(f'Missing landmark - {landmark}.')
    return landmarks

def landmarks2dict(landmarks: Image33LandMarks) -> dict:
    posedict = {}
    for landmark in landmarks.getlandmarknames():
        posedict[landmark] = landmarks.getlandmark(landmark).getposition()
    return posedict

def dict2angles(angles: dict) -> Angles:
    anglesobj = Angles()
    for angle in anglesobj.angle_names:
        try:
            angles.setangle(angle, angles[angle])
        except:
            print(f'Missing Angle - {angle}.')
    return anglesobj

def angles2dict(angles: Angles) -> dict:
    anglesdict = {}
    for angle in angles.angle_names:
        anglesdict[angle] = angles.getangle(angle)
    return anglesdict

