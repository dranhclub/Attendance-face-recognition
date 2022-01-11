# Application for attendance by facial recognition
Computer Vision final assignment

## Requirements
- [face_recognition](https://github.com/ageitgey/face_recognition)
- Flask framework to build web app


## Requirements
- face_recognition
- Flask

## How to install face_recognition library
- Visit [face_recognition](https://github.com/ageitgey/face_recognition) for detail
- Following is my way to install face_recognition library in Windows

        conda update ipykernel
        conda update --all

        repeat the above update till no error (took few runs for me), then run:

        conda create -n face_recognition python==3.6.6 anaconda
        conda activate face_recognition
        pip install cmake
        pip install dlib==19.8.1
        pip install face_recognition
        pip install opencv-contrib-python==4.1.0.25
        pip install twisted

- cre: https://github.com/ageitgey/face_recognition/issues/175#issuecomment-636287794


## How to run
- Run with cmd:
- `cd` to project directory
- `set FLASK_APP=diemdanh`
- `set FLASK_ENV=development`
- Init database before run (optional): `flask init-db`
- `flask run`

