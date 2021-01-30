from flask import Flask, render_template, request,make_response,jsonify,redirect,url_for
#from flask_cors import CORS
import os
#import resnet
import skincancerclassifier
import json
import numpy as np
import tensorflow as tf

#UPLOAD_FOLDER = 'uploads/'
#ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
#CORS(app)

#fileNameList = []
#resnetmodel = resnet.load_model()
s = skincancerclassifier.SkinCancerClassifier()
s.load_models()
#out = s.run('test_nvv.jpg',[0,0,1])
#print("OUT:", out)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
fileNameList = []
modelResults = []
tempopt = []
options = []
result = []


'''result = [
                    [
                        'ResNet152V2', 
                        ('nv', 'melanocytic nevi', 0.9999974), 
                        ('bkl', 'benign keratosis-like lesions,seborrheic', 2.5060908e-17), 
                        ('akiec', "Actinic keratoses,Bowen's disease", 1.4720392e-07)
                    ], 
                    [
                        'InceptionResNetV2', 
                        ('nv', 'melanocytic nevi', 1.0), 
                        ('mel', 'melanoma', 2.9319884e-15), 
                        ('bkl', 'benign keratosis-like lesions, solar lentigines / seborrheic keratoses and lichen-planus like keratoses', 8.238215e-15)
                    ],
                    [
                        'InceptionV3', 
                        ('nv', 'testingval1', 1.0), 
                        ('mel', 'ieirheurhehr', 1.0), 
                        ('bkl', 'keratoses', 1.0)
                    ]

]'''
#this is where the image gets accepted and placed into a folder within the application
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
       for file in request.files.getlist("image_file"):
            print("FILE", file)
            path = (os.path.join(UPLOAD_FOLDER, file.filename))
            file.save(path)
            fileNameList.append(path)
       return jsonify({"msg":"OK"})

#this is the post request after selecting the algos, which creates an array of 1 and 0's.
@app.route('/algos', methods=['GET', 'POST'])
def algos():
 
    
    if request.method == 'POST':
        s.load_models()
        req = request.get_json()
        global result
        
        
        print("REQ", req)
        global options
        options = []
        for value in req.values():
            
            if value == True:
                options.append(1)
            else:
                options.append(0)
        
        print("Options", options)
        #this is where the array  of 1 and 0's will get sent to the actual algorithms and begin the processing.
        result = s.run(fileNameList[0],options)
         
        

        
        return jsonify({"msg":"OK"})
@app.route('/results', methods=['GET'])
def results():
    print("RESULT in post results", result)
    response = { 'msg': result }
    return jsonify(response)
    #return json.dumps(response)

@app.route('/array', methods=['GET'])
def getArray():
    
    response = {"optionarray": options}

    return jsonify(response)

if __name__ == '__main__' :
    app.run()