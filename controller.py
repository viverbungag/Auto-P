from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
from pynput import keyboard
from pynput.keyboard import Key, Controller

checker = False

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear



def startController():
    keyboard = Controller()

    EYE_AR_THRESH = 0.40
    EYE_AR_CONSEC_FRAMES = 10
    FRAME_BEFORE_PAUSE = 30

    COUNTER = 0

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    vs = VideoStream(src=0).start()
    time.sleep(1.0)

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR)

            if ear < EYE_AR_THRESH:

                COUNTER += 1

                if (COUNTER > FRAME_BEFORE_PAUSE):
                    keyboard.press(',')
                    keyboard.release(',')

            else:
                COUNTER = 0
                keyboard.press('.')
                keyboard.release('.')
                
        key = cv2.waitKey(1) & 0xFF
        # threadLock.acquire()
        print(checker)
        if checker:
            print("stopped1")
            break
        # threadLock.release()

    cv2.destroyAllWindows()
    vs.stop()

def on_release(key):
    if key == keyboard.Key.esc:
        print("stopped2")
        checker = True
        return False

def startListener():
    with keyboard.Listener(
            on_release=on_release) as listener:
        listener.join()


    listener = keyboard.Listener(
        on_release=on_release)
    listener.start()   

# if __name__ == '__main__':
# threadLock = threading.Lock()





