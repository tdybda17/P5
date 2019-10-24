import os

from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator



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


def getfitgenerator(classifier, trainingset, testset):
    return classifier.fit_generator(trainingset,
                             samples_per_epoch=6000,
                             # integer, number of samples to process before starting a new epoch.
                             nb_epoch=1,
                             validation_data=testset,
                             nb_val_samples=2000)  # number of samples to use from validation generator at the end of every epoch.

def gettraindatagen(train_datagen):
    return train_datagen.flow_from_directory('../../files/images/dataset-resized/training_data',
                                      target_size=(128, 128),
                                      batch_size=32,
                                      class_mode='categorical')

def gettestdatagen(test_datagen):
    return test_datagen.flow_from_directory('../../files/images/dataset-resized/test_data',
                                            target_size = (128, 128),
                                            batch_size = 32,
                                            class_mode = 'categorical')
def getimagedatagen():
    return ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

def getrescalegen():
    return ImageDataGenerator(rescale = 1./255)


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


