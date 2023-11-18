from Interface.utils import dict2landmarks
from Core.poselandmarks import Image33LandMarks
from Core.landmark import Landmark
import pytest

def test_dict2landmarks():
    poses = {
        'nose': (0,0), 
        'left eye (inner)': (0,0), 
        'left eye': (0,0), 
        'left eye (outer)': (0,0), 
        'right eye (inner)': (0,0), 
        'right eye': (0,0), 
        'right eye (outer)': (0,0),
        'left ear': (0,0),
        'right ear': (0,0),
        'mouth (left)': (0,0),
        'mouth (right)': (0,0),
        'left shoulder': (0,0),
        'right shoulder': (0,0),
        'left elbow': (0,0),
        'right elbow': (0,0),
        'left wrist': (0,0),
        'right wrist': (0,0),
        'left pinky': (0,0),
        'right pinky': (0,0),
        'left index': (0,0),
        'right index': (0,0),
        'left thumb': (0,0),
        'right thumb': (0,0),
        'left hip': (0,0),
        'right hip': (0,0),
        'left knee': (0,0),
        'right knee': (0,0),
        'left ankle': (0,0),
        'right ankle': (0,0),
        'left heel': (1,0),
        'right heel': (0,0),
        'left foot index': (0,0),
        'right foot index': (0,0)
    }
    poseobj = dict2landmarks(poses)
    assert isinstance(poseobj, Image33LandMarks) is True
    assert isinstance(poseobj.getlandmark('left heel'), Landmark) is True
    assert isinstance(poseobj.getlandmark('left heel').getposition(), tuple) is True
    assert poseobj.getlandmark('left heel').getposition()[0] == 1