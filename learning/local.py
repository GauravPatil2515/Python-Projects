# f =open("myfile.txt","r")

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break
#     print(line)

import mediapipe as mp

# Initialize the face detector
mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Read in an image
image = mp.Image(filename="test.jpg")

# Detect faces in the image
results = face_detection.process(image)

# Draw bounding boxes around detected faces
if results.detections:
  for detection in results.detections:
    mp_drawing.draw_detection(image, detection)

# Display the image with detected faces
image.show()