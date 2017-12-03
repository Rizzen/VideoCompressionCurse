import Compression as comp
from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


# http://127.0.0.1:5000/video_feed
@app.route('/video_feed')
def video_feed():
    res = Response(comp.gen(comp.IPCamVideo()), mimetype='multipart/x-mixed-replace; boundary=frame')
    return res


if __name__ == '__main__':
    app.run()
