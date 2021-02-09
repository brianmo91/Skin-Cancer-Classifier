from keras.applications.resnet_v2 import ResNet152V2
from keras.preprocessing import image
from keras.applications.resnet_v2 import preprocess_input
from keras.layers import Input
from util import map_scores
from pathlib import Path
import numpy as np
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=config))

def load_model(dim_size=224):
    input_tensor = Input(shape=(dim_size, dim_size, 3))
    model = ResNet152V2(input_tensor=input_tensor, weights=None, classes=7)
    model.load_weights('resnet_weights320.h5', by_name=False)
    return model

def load_image(img_path, dim_size=224):
    img = image.load_img(img_path, target_size=(dim_size, dim_size))
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)
    return x

def predict(x, model):
    preds = model.predict(x)
    return map_scores(preds,3)[0]

def run(path,model):
    x = load_image(path)
    return predict(x,model)