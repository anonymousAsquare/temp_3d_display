import mediapipe as mp
import cv2
from vpython import *
import numpy as np

window_width = 640
window_height = 480
fps = 30

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class mp_handlm():
    import mediapipe as mp
    def __init__(self):
        self.mp_hand = self.mp.solutions.hands.Hands(False,1,.5,.5)
        self.mp_handDraw = self.mp.solutions.drawing_utils

    def handMl(self, frame):
        landmarks = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.mp_hand.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_handDraw.draw_landmarks(frame,hand_landmarks,self.mp.solutions.hands.HAND_CONNECTIONS)
                landmark = []
                for hand_landmark in hand_landmarks.landmark:
                    landmark.append(((hand_landmark.x),(hand_landmark.y),(hand_landmark.z)))
                landmarks.append(landmark)
        return landmarks

landmarks = mp_handlm()

h = []
for i in range(0,21,1):
    h.append(sphere(radius = .02, pos = vector(0,0,0)))

while True:
    ignore, frame = cam.read()
    hand_data_ = landmarks.handMl(frame)

    if hand_data_ != None:
        for hand_data in hand_data_:
            for data,i in zip(hand_data,h):
                i.pos = vector(data[0],-(data[1]), data[2])
                print(data)

    cv2.imshow('Asquare', frame)
    #cv2.moveWindow('Asquare', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        cv2.destroyAllWindows
        break
cam.release()