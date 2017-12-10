import cv2
import time
import requests
import VideoWriter
import ffmpy


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
            ret, jpeg = cv2.imencode('.jpg', image)
            var = 0.04 - (time.time() - current_time)
            if var > 0:
                time.sleep(var)
            return jpeg.tobytes(), success
        return None, success


# using requests to capture video via smartphone with IPWebcam
class IPCamVideo(object):

    def __init__(self):
        self.url = 'http://192.168.100.7:8080/shot.jpg'

    def get_frame(self):
        response = requests.get(self.url, stream=True)
        frame = response.content
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes(), True


class CompressedVideoWriter(object):

    def __init__(self):
        self.video = cv2.VideoCapture('E:\PyProjects\Resources\\test.mov')
        self.writer = VideoWriter.Writer()

    def __del__(self):
        self.video.release()
        self.writer.__del__()

    def write_video(self):
        self.writer.write(self.video)


def gen(video):
    while True:
        frame, success = video.get_frame()
        if success:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def cap_and_write(writer):
    writer.write_video()


def just_cap():
    VideoWriter.write()


def comp_ffmpy():
    ff = ffmpy.FFmpeg(
        inputs={'E:\PyProjects\Resources\\test.mov': None},
        outputs={'output.avi': None}
    )
    ff.run()
