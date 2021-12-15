# Ứng dụng điểm danh bằng nhận diện khuôn mặt
Bài tập lớn môn Thị giác máy tính

## Công nghệ sử dụng
- Thư viện [face_recognition](https://github.com/ageitgey/face_recognition)
- Xây dựng website bằng Flask

## How to install face_recognition
https://github.com/ageitgey/face_recognition/issues/175#issuecomment-636287794 


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

## Requirements
- `pip install face_recognition`
- `pip install Flask`

## How to run
- `python app.py`