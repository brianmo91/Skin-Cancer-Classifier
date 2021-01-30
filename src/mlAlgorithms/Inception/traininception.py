from keras.applications.inception_v3 import InceptionV3
from keras_preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from keras.layers import Input
from keras.callbacks import TensorBoard
from os import path
from datetime import datetime
import pandas as pd
import tensorflow as tf
import time

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=config))

log_name = "Dim224_Batch16_RMSprop_"
logdir = "logs/scalars/inception/" + log_name + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=logdir)

dim_size = 224
batch_size = 16
epochs = 200
weights = ''
df = pd.read_csv("train.csv")

datagen = ImageDataGenerator(
   rescale = 1./255,
   shear_range = 0.2,
   zoom_range = 0.2,
   horizontal_flip = True,
   validation_split = 0.1)
train_generator = datagen.flow_from_dataframe(
   dataframe = df, 
   directory = "train_images", 
   x_col = "id", y_col = "label",
   subset="training", 
   class_mode = "categorical", 
   target_size = (dim_size,dim_size), 
   batch_size = batch_size
)
valid_generator = datagen.flow_from_dataframe(
   dataframe = df, 
   directory = "train_images", 
   x_col = "id", y_col = "label",
   subset="validation", 
   class_mode = "categorical", 
   target_size = (dim_size,dim_size), 
   batch_size = batch_size
)

def load_model(dim_size):
   input_tensor = Input(shape=(dim_size, dim_size, 3))
   global model
   model = InceptionV3(input_tensor=input_tensor, weights=None, classes=7)

   if path.exists(weights):
      model.load_weights(weights, by_name=False)

   #for layer in model.layers[:551]:
   #   layer.trainable = False
   #for layer in model.layers[551:]:
   #   layer.trainable = True
   for layer in model.layers:
      layer.trainable = True

   model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=["accuracy"])
   #from keras.optimizers import SGD
   #model.compile(optimizer=SGD(lr=0.01, momentum=0.9), loss='categorical_crossentropy')

def list_layers():
   for i, layer in enumerate(model.layers):
      print(i, layer.name)

def train():
   STEP_SIZE_TRAIN = train_generator.n//train_generator.batch_size
   STEP_SIZE_VALID = valid_generator.n//valid_generator.batch_size
   training_history = model.fit_generator(
      generator=train_generator,
      steps_per_epoch=STEP_SIZE_TRAIN,
      validation_data=valid_generator,
      validation_steps=STEP_SIZE_VALID,
      epochs=epochs,
      callbacks=[tensorboard_callback]
   )

   model.save_weights('weights_inception224.h5')

if __name__== "__main__":
   start_time = time.time()
   load_model(dim_size)
   train()
   elapsed_time = time.time() - start_time
   print('Runtime: ', elapsed_time)
  