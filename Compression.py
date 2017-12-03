from flask import Flask, render_template, Response
import cv2
import urllib
import requests
import numpy as np


# Opens video and shows it in browser
class Video(object):

    def __init__(self):
        self.video = cv2.VideoCapture('E:\PyProjects\Compression\\123.webm')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if success:
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes(), success
        return None, False


# using requests to capture video via smartphone with IPWebcam
class IPCamVideo(object):
    def __init__(self):
        self.url = 'http://192.168.100.7:8080/shot.jpg'

    def get_frame(self):
        responce = requests.get(self.url, stream=True)

        return responce.content, True


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


def gen(video):
    while True:
        frame, success = video.get_frame()
        if success:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# http://127.0.0.1:5000/video_feed
@app.route('/video_feed')
def video_feed():
    res = Response(gen(IPCamVideo()), mimetype='multipart/x-mixed-replace; boundary=frame')
    return res


if __name__ == '__main__':
    app.run()
