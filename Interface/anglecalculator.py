from Core.media import Media
from Core.poselandmarks import Image33LandMarks
from UseCases.calculateposes import PoseCalculator
from UseCases.calculateangles import AngleCalculator
from Interface.utils import dict2landmarks, angles2dict
from abc import ABC, abstractmethod
import numpy as np
# import json

class PoseCalculatorFromNPArray():
    @abstractmethod
    def calculate33posefromnp(self, frame: np.array) -> dict:
        pass

class AngleCalculatorFromNPArray:
    
    def __init__(self, frame: np.array, posecalculator: PoseCalculatorFromNPArray) -> None:
        self._frame = frame
        self.posecalculator = posecalculator
        self.calculator = AngleCalculator()

    def calculateangle(self) -> dict:
        poses = self.posecalculator.calculate33posefromnp(self._frame)
        anglesobj = self.calculator.calculateangles(dict2landmarks(poses))
        return angles2dict(anglesobj)