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


def write():
    cap = cv2.VideoCapture('E:\PyProjects\Resources\\test.mov')
    ret, frame = cap.read()

    FPS = 20.0
    FrameSize = (frame.shape[1], frame.shape[0])  # MUST set or not thing happen !!!! vtest is 768,576.
    isColor = 1  # flag for color(true or 1) or gray (0)
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter('Video_output.avi', fourcc, FPS, FrameSize)

    while cap.isOpened():
        ret, frame = cap.read()

        # Save the video
        out.write(frame)  # It's not work without proper size of frame

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()