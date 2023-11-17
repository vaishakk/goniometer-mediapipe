from Core.poselandmarks import Image33LandMarks
from Core.landmark import Landmark
import pytest

def test_init():
    imagelandmarks = Image33LandMarks('testpath')
    assert len(imagelandmarks.getlandmarks().keys()) == 33
    assert isinstance(imagelandmarks.getlandmarks()['nose'], Landmark) is True
    assert imagelandmarks.getmedia().getpath() == 'testpath'