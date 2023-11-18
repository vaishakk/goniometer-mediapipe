import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import cv2
import numpy as np

def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image

def getmediapipeposes(data: np.array):

    model_path = '/Users/vk/dev/PoseEstimation/External/pose_landmarker_full.task'

    BaseOptions = mp.tasks.BaseOptions
    PoseLandmarker = mp.tasks.vision.PoseLandmarker
    PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    options = PoseLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.IMAGE)
    
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=data)
    print(data.shape)
    with PoseLandmarker.create_from_options(options) as landmarker:
        pose_landmarker_result = landmarker.detect(image)
        annotated_image = draw_landmarks_on_image(image.numpy_view(), pose_landmarker_result)
        #cv2.imshow('',cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
        cv2.imshow('',annotated_image)
        #cv2.waitKey()
    return pose_landmarker_result

def poselandmarkerresult2dict(result) -> dict:
   posedict = {}
   landmark_names = [
        'nose', 
        'left eye (inner)', 
        'left eye', 
        'left eye (outer)', 
        'right eye (inner)', 
        'right eye', 
        'right eye (outer)',
        'left ear',
        'right ear',
        'mouth (left)',
        'mouth (right)',
        'left shoulder',
        'right shoulder',
        'left elbow',
        'right elbow',
        'left wrist',
        'right wrist',
        'left pinky',
        'right pinky',
        'left index',
        'right index',
        'left thumb',
        'right thumb',
        'left hip',
        'right hip',
        'left knee',
        'right knee',
        'left ankle',
        'right ankle',
        'left heel',
        'right heel',
        'left foot index',
        'right foot index'
        ]
   landmark_list = result.pose_landmarks[0]
   for idx, landmark in enumerate(landmark_list):
      posedict[landmark_names[idx]] = (landmark_list[idx].x, landmark_list[idx].y)
   return posedict

data = cv2.imread('/Users/vk/dev/PoseEstimation/External/test_img.jpg', 1)
print(poselandmarkerresult2dict(getmediapipeposes(data)))