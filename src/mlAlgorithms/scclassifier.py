import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from keras.applications.resnet_v2 import ResNet152V2
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.layers import Input
from util import map_scores
import numpy as np
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=config))

class SkinCancerClassifier():
    def __init__(self, dim_size=224):
        self.resnet = None
        self.inception = None
        self.inceptionresnet = None
        self.dim_size = dim_size

    def load_models(self):
        input_tensor = Input(shape=(self.dim_size, self.dim_size, 3))
        self.resnet = ResNet152V2(input_tensor=input_tensor, weights=None, classes=7)
        self.resnet.load_weights('weights_resnet224.h5', by_name=False)
        self.inception = InceptionV3(input_tensor=input_tensor, weights=None, classes=7)
        self.inception.load_weights('weights_inception224.h5', by_name=False)
        self.inceptionresnet = InceptionResNetV2(input_tensor=input_tensor, weights=None, classes=7)
        self.inceptionresnet.load_weights('weights_inceptionresnet224.h5', by_name=False)

    def load_image(self,img_path):
        img = image.load_img(img_path, target_size=(self.dim_size, self.dim_size))
        x = image.img_to_array(img)
        x = x / 255.0
        x = np.expand_dims(x, axis=0)
        return x

    def run(self,path,choice=[0,0,0],top=3):
        preds = []
        x = self.load_image(path)
        if choice[0] == 1:
            preds.extend(self.resnet.predict(x))
        if choice[1] == 1:
            preds.extend(self.inception.predict(x))
        if choice[2] == 1:
            preds.extend(self.inceptionresnet.predict(x))
        scores = map_scores(preds,top)
        return scores