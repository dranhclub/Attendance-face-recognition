from core import generate_frames, attendence_set, known_face_names
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', known_face_names=known_face_names)


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/listen')
def listen():
    global count
    return {"attendence_list": list(attendence_set)}


def main():
    app.run(port=5000, debug=False)


if __name__ == "__main__":
    main()
