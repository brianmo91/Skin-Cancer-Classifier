import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from keras.applications.resnet_v2 import ResNet152V2
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.layers import Input
from util import map_scores
import numpy as np
#import tensorflow as tf
import time

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#config = tf.ConfigProto()
#config.gpu_options.allow_growth = True
#tf.keras.backend.set_session(tf.Session(config=config))

class SkinCancerClassifier():
    def __init__(self, dim_size=224):
        self.resnet = None
        self.inception = None
        self.inceptionresnet = None
        self.dim_size = dim_size

    def load_models(self):
        """
        Instantiates models and loads the weights.
        **MUST LOAD BEFORE RUNNING MODELS**
        """
        input_tensor = Input(shape=(self.dim_size, self.dim_size, 3))
        self.resnet = ResNet152V2(input_tensor=input_tensor, weights=None, classes=7)
        self.resnet.load_weights('weights_resnet224.h5', by_name=False)
        self.inception = InceptionV3(input_tensor=input_tensor, weights=None, classes=7)
        self.inception.load_weights('weights_inception224.h5', by_name=False)
        self.inceptionresnet = InceptionResNetV2(input_tensor=input_tensor, weights=None, classes=7)
        self.inceptionresnet.load_weights('weights_inceptionresnet224.h5', by_name=False)
        

    def load_image(self,img_path):
        """
        Preprocesses an image for input to model
        
        # Arguments
            img_path: String path to image

        # Returns
            An array of processed image scaled by 1/255
        """
        img = image.load_img(img_path, target_size=(self.dim_size, self.dim_size))
        x = image.img_to_array(img)
        x = x / 255.0
        x = np.expand_dims(x, axis=0)
        return x

    def run(self,path,choice=[0,0,0],top=3):
        """
        Inputs image and predicts using selected model
        
        # Arguments
            path: String path to image
            choice: Array of binary values for selecting models to infer.
                Each index of array used to represent a model.
                Ex:
                    [1, 1, 1] toggles [ResNet152V2, InceptionV3, InceptionResNetV2]'
            top: Integer indicating the top 'X' classes of prediction.

        # Returns
            A list of lists of model name and top class prediction tuples
            Ex:
                path = 'image_path'
                choice = [1,0,1]
                top = 3

                [
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
                    ]
                ]
        """
        
        preds = []
        x = self.load_image(path)
        if choice[0] == 1:
            arr = ['ResNet152V2']
            arr.extend(self.resnet.predict(x))
            preds.append(arr)
        if choice[1] == 1:
            arr = ['InceptionV3']
            arr.extend(self.inception.predict(x))
            preds.append(arr)
        if choice[2] == 1:
            arr = ['InceptionResNetV2']
            arr.extend(self.inceptionresnet.predict(x))
            preds.append(arr)
        scores = map_scores(preds,top)
        return scores
        

        

if __name__ == "__main__":
    print('Loading...')
    load_time1 = time.time()
    scc = SkinCancerClassifier()
    scc.load_models()
    load_time2 = time.time()
    print('Loaded')
    print('Loadtime: ', load_time2-load_time1)

    print('\nRunning...')
    start_time = time.time()
    out = scc.run('test_nvv.jpg',[0,0,1])
    end_time1 = time.time()
    print('001: ',out)
    print('Runtime: ', end_time1-start_time)

    print('\nRunning...')
    out1 = scc.run('test_nvv.jpg',[1,0,1])
    end_time2 = time.time()
    print('101: ',out1)
    print('Runtime: ', end_time2-end_time1)

    print('\nRunning...')
    out2 = scc.run('test_nvv.jpg',[1,1,1])
    end_time3 = time.time()
    print('111: ',out2)
    print('Runtime: ', end_time3-end_time2)