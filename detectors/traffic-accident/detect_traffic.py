import tensorflow as tf
import efficientnet.keras
import efficientnet.tfkeras
from PIL import Image
import numpy as np
import argparse
import os

cwd = os.getcwd()
print(cwd + "/traffic-net10.h5")

parser = argparse.ArgumentParser()
parser.add_argument("image_path", help="Input path to image you want to predict")
args = parser.parse_args()
img = Image.open(args.image_path)
new_img = np.array(img.resize((224,224)))
new_img = np.expand_dims(new_img, axis=0)

model = tf.keras.models.load_model(cwd + "/traffic-net10.h5")
print("Accident Probability:", 1- model.predict(new_img))
