from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input
import os
import pickle
import numpy as np
from keras import backend as K
K.clear_session()
class my_pne_predictor():
  def __init__(self, file):
    self.file = file

  def deserialize(self):
    filename = 'final1.sav' #path to the saved model
    print('loading')
    model = pickle.load(open(filename, 'rb'))
    return model

  def predict(self):
    print('predicting')
    model = self.deserialize()
    img = image.load_img(self.file, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    K.clear_session()
    y_classes = preds.argmax(axis=-1)
    return y_classes[0]
