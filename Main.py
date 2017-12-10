import Compression as compression
from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


# http://127.0.0.1:5000/video_feed
@app.route('/video_feed')
def video_feed():
    res = Response(compression.gen(compression.Video()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')
    return res


# http://127.0.0.1:5000/camera
@app.route('/camera')
def camera():
    res = Response(compression.gen(compression.IPCamVideo()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')
    return res


# http://127.0.0.1:5000/video_write
@app.route('/video_write')
def video_write():
    compression.cap_and_write(compression.CompressedVideoWriter())
    return 'Done!'


# http://127.0.0.1:5000/ffmpy
@app.route('/ffmpy')
def ffmpy():
    compression.comp_ffmpy()
    return 'Done!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
