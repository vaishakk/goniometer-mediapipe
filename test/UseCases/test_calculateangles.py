from UseCases.calculateangles import AngleCalculator
from Core.poselandmarks import Image33LandMarks
import pytest

def test_calculateanglefrompoints():
    calculator = AngleCalculator()
    assert pytest.approx(calculator.calculateanglefrompoints((1, 0),(0, 1),(0, 0)), 0.12) == 1.57

def test_calculateanglefromposes():
    poses = Image33LandMarks(imagepath='')
    calculator = AngleCalculator()
    poses.setlandmark(pose= 'left shoulder', position=(1,1))
    poses.setlandmark(pose= 'left wrist', position=(1,0))
    poses.setlandmark(pose= 'left elbow', position=(0,0))
    assert pytest.approx(calculator.calculateanglefromposes('elbowLeft', poses), .12) == 0.78