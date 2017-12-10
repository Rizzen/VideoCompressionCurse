import cv2
import numpy as np


class Writer(object):

    def __init__(self):
        # 'M', 'J', 'P', 'G'
        # D', 'I', 'V', 'X'
        self.fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        #
        self.out = cv2.VideoWriter('output.avi', self.fourcc, 25.0, (720, 576))

    def __del__(self):
        self.out.release()

    def write(self, cap):
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, jpeg = cv2.imencode('.jpg', frame)
                # frame = cv2.flip(frame, 0)
                # write the flipped frame
                self.out.write(frame)
            else:
                break
