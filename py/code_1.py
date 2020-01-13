# -*- coding: utf-8 -*-
"""Code-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KFmpuex_uJCiZYQDJgzBvVJDT3vLryFU
"""

import numpy as np
import matplotlib.pyplot as plt

#from glob import glob
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from keras.layers import BatchNormalization, Dropout

from google.colab import drive
drive.mount('/content/drive')

data=ImageDataGenerator()

train = data.flow_from_directory('/content/drive/My Drive/CDAC Project/Dataset/Train/', class_mode= 'binary',batch_size=4620,target_size=(224,224))

test = data.flow_from_directory('/content/drive/My Drive/CDAC Project/Dataset/Test/', class_mode = 'binary',batch_size=1375, target_size=(224,224))

print(train.image_shape)
print(test.image_shape)

from keras.applications.resnet50 import ResNet50

model = ResNet50(weights='imagenet')

train_x, train_y = train.next()

from scipy import ndimage, misc

model.summary()

print(train_x.shape)







print('Batch shape=%s, min=%.3f, max=%.3f' % (train_x.shape, train_x.min(), train_x.max()))
print('Batch shape=%s, min=%.3f, max=%.3f' % (train_y.shape, train_y.min(), train_y.max()))

test_x, test_y = test.next()

print('Batch shape=%s, min=%.3f, max=%.3f' % (test_x.shape, test_x.min(), test_x.max()))
print('Batch shape=%s, min=%.3f, max=%.3f' % (test_y.shape, test_y.min(), test_y.max()))

from scipy import ndimage







# input_shape = (256, 256, 3)

# model = Sequential()

# model.add(Conv2D(input_shape = input_shape, filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same', kernel_initializer='he_normal'))

# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same', kernel_initializer='he_normal'))
# model.add(Conv2D(filters = 25, kernel_size = (1,1), strides = (1,1), padding = 'valid', kernel_initializer='he_normal'))
# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size = (2,2)))
# model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same', kernel_initializer='he_normal'))
# model.add(Conv2D(filters = 25, kernel_size = (1,1), strides = (1,1), padding = 'valid', kernel_initializer='he_normal'))
# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same', kernel_initializer='he_normal'))
# model.add(Conv2D(filters = 25, kernel_size = (1,1), strides = (1,1), padding = 'valid', kernel_initializer='he_normal'))
# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size = (2,2)))
# model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same', kernel_initializer='he_normal'))
# model.add(Conv2D(filters = 25, kernel_size = (1,1), strides = (1,1), padding = 'valid', kernel_initializer='he_normal'))
# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same', kernel_initializer='he_normal'))
# model.add(Conv2D(filters = 25, kernel_size = (1,1), strides = (1,1), padding = 'valid', kernel_initializer='he_normal'))
# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size = (2,2)))


# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(2, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_x, train_y, batch_size = 128, epochs = 1, verbose = 1)

model.evaluate(test_x, test_y)

