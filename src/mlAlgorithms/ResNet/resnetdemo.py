from keras.applications.resnet_v2 import ResNet152V2
from keras.preprocessing import image
from keras.applications.resnet_v2 import preprocess_input
from keras.layers import Input
from util import map_scores
from pathlib import Path
import numpy as np
import tensorflow as tf
import time

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=config))

start_time = time.time()

dim_size = 224
input_tensor = Input(shape=(dim_size, dim_size, 3))

model = ResNet152V2(input_tensor=input_tensor, weights=None, classes=7)
model.load_weights('resnet_weights320.h5', by_name=False)

img_path = str(Path(__file__).resolve().parents[1]) + '/test_imgs/mela1.jpg'
img = image.load_img(img_path, target_size=(dim_size, dim_size))
x = image.img_to_array(img)
x = x / 255.0
x = np.expand_dims(x, axis=0)
#x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', map_scores(preds,3)[0])

elapsed_time = time.time() - start_time
print('Runtime: ', elapsed_time)