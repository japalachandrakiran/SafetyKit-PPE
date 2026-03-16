from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# load your PPE model
model = YOLO(r"/home/hypervise/pasco techtrack/safetykitPPE/best.pt")

camera = cv2.VideoCapture(0)  # change if RTSP camera

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # run inference
        results = model(frame, conf=0.4)

        for r in results:
            frame = r.plot()

        # encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)