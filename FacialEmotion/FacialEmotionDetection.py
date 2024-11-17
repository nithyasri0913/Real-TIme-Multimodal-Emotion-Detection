import os.path
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import fer
import tensorflow as tf
import keras
from keras import layers
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

'''img_array = cv2.imread("train/angry/Training_3908.jpg")
print(img_array.shape)
plt.imshow(img_array)
plt.show()'''

# declare dataset and categories
dataset = "train/"
classes = ["0", "1", "2", "3"]
'''
#read all images from folders
for category in classes:
    path = os.path.join(dataset, category)
    ImgsInCategory = os.listdir(path)
    for img in ImgsInCategory:
        img_array = cv2.imread(os.path.join(path, img))
        plt.imshow(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))
        plt.show()
        break
    break'''

# change to BGR format and adjust size
img_size = 224
'''new_array = cv2.resize(img_array, (img_size, img_size))
plt.imshow(cv2.cvtColor(new_array, cv2.COLOR_BGR2RGB))
print(new_array.shape)
plt.show()'''

# read all images and convert them to array
training_data = []


# read all images and insert them to list
def create_training_data():
    for category in classes:
        path = os.path.join(dataset, category)
        imgs_in_category = os.listdir(path)
        for img in imgs_in_category:
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, category])
            except Exception as e:
                pass


create_training_data()
print(len(training_data))

# shuffle because it should be in order, not learn sequence
random.shuffle(training_data)

X = []  # data/feature
Y = []  # label

for features, label in training_data:
    X.append(features)
    Y.append(label)

# converting to 4 dimensions
x = np.array(X).reshape(-1, img_size, img_size, 3)
# print(X.shape)

# print(np.shape(training_data))
# print(np.array(training_data).shape)
# print(training_data[0])

# normalize data
x = x / 255.0  ##normalize with skikit learn but for now it is ok (divide by maximal number to normalize)
print(Y[1000])  ## Y is the label

model = tf.keras.applications.MobileNetV2()  # model needs rgb and 224 pre trained model

model.summary()

# transfer learning
base_input = model.layers[0].input
base_output = model.layers[-2].output
print(base_output)

final_output = layers.Dense(128)(base_output)  ##adding new layer after global_average_pooling
final_output = layers.Activation("relu")(final_output)
final_output = layers.Dense(64)(final_output)
final_output = layers.Activation("relu")(final_output)
final_output = layers.Dense(4, activation="softmax")(
    final_output)  ##my classes are 4, classification layer und somit softmax

new_model = keras.Model(inputs=base_input, outputs=final_output)
##new_model.summary()

new_model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
##new_model.summary()

##settings for binary classification
#Y = np.array(Y)

##X = np.array(X)
new_model.fit(X, Y, epochs=25)
new_model.save("my_model.h5")
