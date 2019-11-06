from builtins import len, range

import matplotlib.pyplot as plt
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

from image_compressor.dir_walker.dir_walker import walk_dir

test_size = len(walk_dir(path='../../../files/images/dataset-resized/test_data',files_extensions=['.jpg']))


def get_init_conv_layer(filters, kernel, stride):
    return Conv2D(filters=filters, kernel_size=kernel, strides=stride, input_shape=(112, 200, 3), activation='relu')


def get_conv_layer(filters, kernel, stride):
    return Conv2D(filters=filters, kernel_size=kernel, strides=stride, activation='relu')


def get_maxpool_layer(size):
    return MaxPooling2D(pool_size=(size, size), strides=size)


def get_dropout_layer(dropout):
    return Dropout(dropout)


def get_dense_layer(units):
    return Dense(activation="relu", units=units)


def get_fit_generator(classifier, trainingset, testset):
    return classifier.fit_generator(trainingset,
                             #steps_per_epoch=100,
                             # integer, number of samples to process before starting a new epoch.
                             epochs=100,
                             validation_data=testset,
                             validation_steps= test_size // 32)  # number of samples to use from validation generator at the end of every epoch.


def get_train_data_gen(train_datagen):
    return train_datagen.flow_from_directory('../../../files/images/dataset-resized/dataset-resized/training_data',
                                      target_size=(112, 200),
                                      batch_size=32,
                                      class_mode='categorical')


def get_test_data_gen(test_datagen):
    return test_datagen.flow_from_directory('../../../files/images/dataset-resized/dataset-resized/test_data',
                                            target_size = (112, 200),
                                            batch_size = 32,
                                            class_mode = 'categorical')


def get_image_data_gen():
    return ImageDataGenerator(rescale=1./255,
                                rotation_range=40,
                                width_shift_range=0.2,
                                height_shift_range=0.2,
                                shear_range=0.2,
                                horizontal_flip=True)


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
    plt.ylim(0, 1)
    plt.legend()
    plt.savefig(name)


