from keras.applications.resnet_v2 import ResNet152V2
from keras.preprocessing import image
from keras.applications.resnet_v2 import preprocess_input, decode_predictions
from keras.layers import Input
import numpy as np
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=config))

dim_size = 224
input_tensor = Input(shape=(dim_size, dim_size, 3))

model = ResNet152V2(input_tensor=input_tensor, weights='imagenet')
#model = ResNet152V2(input_tensor=input_tensor, weights=None, classes=7)
#model.load_weights('resnet_weights.h5', by_name=False)

img_path = 'tiger.jpg'
img = image.load_img(img_path, target_size=(dim_size, dim_size))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=5))
# Predicted: 
# [(u'n02504013', u'Indian_elephant', 0.82658225), 
# (u'n01871265', u'tusker', 0.1122357), 
# (u'n02504458', u'African_elephant', 0.061040461)]