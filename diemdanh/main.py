from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response
)
from diemdanh.core import generate_frames, attendence_set
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
import os
from .core import face_encoding, attendence_set
from diemdanh.db import get_db
import json
import numpy as np

bp = Blueprint('diemdanh', __name__)

@bp.route('/')
def index():
    db = get_db()
    students = db.execute(
        'SELECT *'
        ' FROM student'
    ).fetchall()
    return render_template('index.html', students=students)


@bp.route('/video')
def video():
    db = get_db()
    students = db.execute('SELECT * FROM student').fetchall()
    
    list_student = []
    for row in students:
        student = {}
        for key in row.keys():
            student[key] = row[key]
        
        student['encoding_face'] = np.array(json.loads(student['encoding_face']))
        list_student.append(student)

    students = list_student


    return Response(generate_frames(students), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/listen')
def listen():
    return {"attendence_set": list(attendence_set)}


@bp.route('/class-list', methods=('GET', 'POST'))
def class_list():

    db = get_db()
    
    if request.method == 'POST':
        name = request.form['name']
        img = request.form['img']
        try:
            encoding_face = face_encoding(img)
            db.execute('INSERT INTO student (name, img, encoding_face) values (?,?,?)', (name, img, json.dumps(encoding_face.tolist())))
        except IndexError:
            db.execute('INSERT INTO student (name, img, encoding_face) values (?,?,?)', (name, img, None))
        db.commit()

    students = db.execute(
        'SELECT *'
        ' FROM student'
    ).fetchall()

    return render_template('class-list.html', students=students)


@bp.route('/delete/<int:id>')
def delete(id):
    db = get_db()

    db.execute('DELETE FROM student WHERE id=?', (id,))
    db.commit()
    return redirect(url_for('diemdanh.class_list'))
