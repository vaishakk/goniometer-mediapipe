# Python Goniometer using Mediapipe

Toolkit for estimating human joint angles from Mediapipe pose detections. The project combines Google Mediapipe pose landmark models with a small, test-driven Python architecture that exposes reusable building blocks and a minimal Flask service for serving joint-angle measurements.

## Features
- Pose landmark abstractions (`Core/`, `Interface/`, `UseCases/`) with unit tests for deterministic angle math.
- Mediapipe integration that converts detector output into the internal landmark model.
- Angle calculator that reports 12 clinically relevant joint angles (elbows, knees, shoulders, hips, ankles, wrists).
- Optional Flask endpoint for uploading images and receiving angle data plus an annotated image.
- Example utilities for serialising angles and pose landmarks to and from dictionaries.

## Requirements
- Python 3.10 (mediapipe currently targets CPython ≤3.10).
- `pip` or `pipenv` for dependency management.
- Mediapipe pose landmarker model (`pose_landmarker_full.task`). A copy ships in `External/`, but you can fetch the latest release from the [Mediapipe Models repository](https://developers.google.com/mediapipe/solutions/vision/pose_landmarker).

## Installation
1. Clone the repository and create a virtual environment:
   ```bash
   git clone https://github.com/vaishakk/Goniometer-Mediapipe.git
   cd Goniometer-Mediapipe
   python3.10 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify that `External/pose_landmarker_full.task` exists.

## Usage
### Angle calculator from NumPy frames
```python
import cv2
from External.mediapipeposecalculator import MediaPipePoseCalculator
from Interface.anglecalculator import AngleCalculatorFromNPArray

image = cv2.imread("path/to/image.jpg", cv2.IMREAD_COLOR)
pose_calculator = MediaPipePoseCalculator()
angle_output = AngleCalculatorFromNPArray(image, pose_calculator).calculateangle()

print(angle_output.angles)            # Dict of joint angles in degrees
cv2.imwrite("annotated.jpg", angle_output.annotated_image)
```

### Flask API
Run the development server:
```bash
export FLASK_APP=External/flask/app.py
flask run --debug
```

Upload an image with `curl`:
```bash
curl -X POST http://127.0.0.1:5000/upload/file \
     -F "imagefile=@/path/to/image.jpg" \
     -H "Content-Type: multipart/form-data"
```
The response contains the computed angles and the annotated pose image encoded as a JSON list of bytes.

## Project layout
- `Core/`: domain entities such as `Landmark`, `Image33LandMarks`, and `Angles`.
- `UseCases/`: application services for pose and angle computation.
- `Interface/`: adapters that turn Mediapipe outputs into domain objects and angle dictionaries.
- `External/`: Mediapipe runtime integration, Flask sample app, and utility helpers.
- `test/`: pytest suites covering utilities, landmark models, and the angle calculator.

## Running tests
```bash
pytest
```

## Contributing
- Open an issue describing the feature or bugfix you plan to work on.
- Follow the existing module structure and keep business logic covered by tests.
- Format code with standard Python style (`black` or `ruff` are good options) and run `pytest` before submitting a pull request.

## Roadmap & Known Issues
- The Flask service writes diagnostic files (`cv2.jpg`) when processing uploads; replace with structured logging for production use.

