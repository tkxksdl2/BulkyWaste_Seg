import tensorflow as tf
import numpy as np
from numpy import argmax
from tensorflow.keras.models import load_model
from PIL import Image
import warnings

warnings.filterwarnings(action='ignore')
new_model = tf.keras.models.load_model('../my_model')
label_filter = ['침대', '밥상', '서랍장', '수납장', '의자', '선풍기','냉장고', '장롱', '책상', '소파']

def trash_pred(img):
    images = []
    img_resized = img.resize([224,224])
    pixels = np.array(img_resized)
    images.append(pixels)
    X = np.asarray(images, dtype=np.float32)
    xhat = X/ 255.0
    yhat = new_model.predict(xhat)
    return label_filter[np.argmax(yhat)]

path = 'C:\\Users\\oooh3\\PycharmProjects\\djangoProject1\\media\\upload\\images (6).jpg'

img = Image.open(path)
print(trash_pred(img))