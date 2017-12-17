import cv2
import time
import Comparer


# Opens video and shows it in browser
class Video(object):

    def __init__(self):
        self.video = cv2.VideoCapture('E:\PyProjects\Resources\\test.mov')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        current_time = time.time()
        success, image = self.video.read()

        if success:
            ret, jpeg = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 50])

            var = 0.04 - (time.time() - current_time)
            if var > 0:
                time.sleep(var)
            return jpeg.tobytes(), success
        return None, success


class WebCam(object):

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if success:
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes(), success
        return None, success


def gen(video):
    while True:
        frame, success = video.get_frame()
        if success:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
