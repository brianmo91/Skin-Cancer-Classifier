import os
from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from werkzeug.utils import secure_filename
import json
import numpy as np
import skincancerclassifier
import time

UPLOAD_FOLDER = 'static/upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10
app.secret_key = 'nhk221'

s = skincancerclassifier.SkinCancerClassifier()

temp = [
            [
                'ResNet152V2', 
                ('nv', 'melanocytic nevi', 0.9999974), 
                ('bkl', 'benign keratosis-like lesions, solar lentigines / seborrheic keratoses and lichen-planus like keratoses', 2.5060908e-06), 
                ('akiec', "Actinic keratoses and intraepithelial carcinoma / Bowen's disease", 1.4720392e-07)
            ], 
            [
                'InceptionResNetV2', 
                ('nv', 'melanocytic nevi', 1.0), 
                ('mel', 'melanoma', 2.9319884e-13), 
                ('bkl', 'benign keratosis-like lesions, solar lentigines / seborrheic keratoses and lichen-planus like keratoses', 8.238215e-15)
            ],
            [
                'InceptionResNetV2', 
                ('nv', 'melanocytic nevi', 1.0), 
                ('mel', 'melanoma', 2.93203314275306e-13), 
                ('bkl', 'benign keratosis-like lesions, solar lentigines / seborrheic keratoses and lichen-planus like keratoses', 8.23808997906482e-15)
            ]
        ]


def load():
    print('Loading models...')
    load_time1 = time.time()
    s.load_models()
    load_time2 = time.time()
    print('Loaded')
    print('Loadtime: ', load_time2-load_time1)

    print('Running Test...')
    end_time2 = time.time()
    output = s.run('test_nvv.jpg',[1,1,1])
    end_time3 = time.time()
    print('Test Successful')
    print('Runtime: ', end_time3-end_time2)
    print('Total Elapsed: ', end_time3-load_time1)

load()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_choices(arr):
    res=[0,0,0]
    for i in arr:
        res[int(i)] = 1
    return res

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/', methods=["POST","GET"])
def index():
    return render_template('index.html')

@app.route('/results', methods=["POST","GET"])
def results():
    if request.method == "POST":

        choices = get_choices(request.form.getlist('nn'))

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(url_for("index"))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No file selected', 'warning')
            return redirect(url_for("index"))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

            #output = temp
            output = s.run(path,choices)
            #os.remove(path)
            return render_template('results.html', output=output, image=path)
        else:
            flash('Only image files allowed', 'warning')
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)