import os

from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Dense
import matplotlib.pyplot as plt
import time


def getinitconvlayer(filters, kernel, stride):
    return Convolution2D(filters, kernel, stride, input_shape=(128, 128, 3), activation='relu')


def getconvlayer(filters, kernel, stride):
    return Convolution2D(filters, kernel, stride, activation='relu')


def getmaxpoollayer(size):
    return MaxPooling2D(pool_size=(size, size))


def getdropoutlayer(dropout):
    return Dropout(dropout)


def getdenselayer(units):
    return Dense(activation="relu", units=units)


def createplot(history):
    history_dict = history.history
    history_dict.keys()

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)
    plt.clf()
    # "bo" is for "blue dot"
    plt.plot(epochs, acc, 'bo', label='Training acc')
    # b is for "solid blue line"
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation acc')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('1')


