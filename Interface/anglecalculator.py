from Core.media import Media
from Core.poselandmarks import Image33LandMarks
from UseCases.calculateposes import PoseCalculator
from UseCases.calculateangles import AngleCalculator
from Interface.utils import dict2landmarks, angles2dict
from abc import ABC, abstractmethod
import numpy as np
# import json

class PoseOutput:
    def __init__(self, poses, annotated_image) -> None:
        self.poses: dict = poses
        self.annotated_image: np.array = annotated_image

class AngleOutput:
    def __init__(self, angles, annotated_image) -> None:
        self.angles: dict = angles
        self.annotated_image: np.array = annotated_image
    

class PoseCalculatorFromNPArray():
    @abstractmethod
    def calculate33posefromnp(self, frame: np.array) -> PoseOutput:
        pass

class AngleCalculatorFromNPArray:
    
    def __init__(self, frame: np.array, posecalculator: PoseCalculatorFromNPArray) -> None:
        self._frame = frame
        self.posecalculator = posecalculator
        self.calculator = AngleCalculator()

    def calculateangle(self) -> AngleOutput:
        poses = self.posecalculator.calculate33posefromnp(self._frame)
        anglesobj = self.calculator.calculateangles(dict2landmarks(poses.poses))
        return AngleOutput(angles2dict(anglesobj), poses.annotated_image)