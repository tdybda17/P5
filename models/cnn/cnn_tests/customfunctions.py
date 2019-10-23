from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Dense


def getinitconvlayer(filters, kernel, stride):
    return Convolution2D(filters, kernel, stride, input_shape=(200, 112, 3), activation='relu')


def getconvlayer(filters, kernel, stride):
    return Convolution2D(filters, kernel, stride, activation='relu')


def getmaxpoollayer(size):
    return MaxPooling2D(pool_size=(size, size))


def getdropoutlayer(dropout):
    return Dropout(dropout)


def getdenselayer(units):
    return Dense(activation="relu", units=units)
