import os

from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator


def get_init_conv_layer(filters, kernel, stride):
    return Conv2D(filters, (kernel, stride), input_shape=(128, 128, 3), activation='relu')


def get_conv_layer(filters, kernel, stride):
    return Conv2D(filters, (kernel, stride), activation='relu')


def get_maxpool_layer(size):
    return MaxPooling2D(pool_size=(size, size))


def get_dropout_layer(dropout):
    return Dropout(dropout)


def get_dense_layer(units):
    return Dense(activation="relu", units=units)


def get_fit_generator(classifier, trainingset, testset):
    return classifier.fit_generator(trainingset,
                             # steps_per_epoch=6000,
                             # integer, number of samples to process before starting a new epoch.
                             epochs=5,
                             validation_data=testset)
                             # validation_steps=2000)  # number of samples to use from validation generator at the end of every epoch.


def get_train_data_gen(train_datagen):
    return train_datagen.flow_from_directory('../../files/images/dataset-resized/training_data',
                                      target_size=(128, 128),
                                      batch_size=32,
                                      class_mode='categorical')


def get_test_data_gen(test_datagen):
    return test_datagen.flow_from_directory('../../files/images/dataset-resized/test_data',
                                            target_size = (128, 128),
                                            batch_size = 32,
                                            class_mode = 'categorical')


def get_image_data_gen():
    return ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)


def get_rescale_gen():
    return ImageDataGenerator(rescale = 1./255)


def create_plot(history, name):
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
    plt.savefig(name)


