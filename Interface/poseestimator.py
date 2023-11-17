from UseCases.calculateposes import PoseCalculator
from UseCases.calculateangles import AngleCalculator
from abc import ABC, abstractmethod

class PoseEstimatorFromFile:
    
    
    def __init__(self, url: str) -> None:
        self._fileurl = url
        self.estimator = PoseCalculator(self._fileurl)

    @abstractmethod
    def generatepose(self) -> list:
        return