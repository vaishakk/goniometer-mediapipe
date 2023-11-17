from abc import ABC, abstractmethod
from Core.media import Media
from Core.poselandmarks import Image33LandMarks

class PoseCalculator:

    @abstractmethod
    def calculate33poseforimage(self, image: Media) -> Image33LandMarks:
        pass
