import Compression as compression
from flask import Flask, Response
import Compare

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


# http://127.0.0.1:5000/web_camera
@app.route('/web_camera')
def web_camera():
    res = Response(compression.gen(compression.WebCam()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')
    return res


# http://127.0.0.1:5000/compare
@app.route('/compare')
def compare():
    res = Response(Compare.gen(Compare.Compare()))
    return res


if __name__ == '__main__':
    # app.run(host='0.0.0.0', threaded=True)
    app.run()
