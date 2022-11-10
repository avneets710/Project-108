import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils

hands=mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)

while True:
    success, image = cap.read()
    results=hands.process(image)
    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

