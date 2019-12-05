from builtins import len, range

import matplotlib.pyplot as plt
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

from image_compressor.dir_walker.dir_walker import walk_dir

image_size_x = 150
image_size_y = 150
epochs = 50
batch_size = 32
test_size = len(walk_dir(path='../../../images/dataset_1920x840/test', files_extensions=['.jpg']))


def get_init_conv_layer(filters, kernel, stride):
    return Conv2D(filters=filters, kernel_size=kernel, strides=stride, input_shape=(image_size_y, image_size_x, 3),
                  activation='relu')


def get_conv_layer(filters, kernel, stride):
    return Conv2D(filters=filters, kernel_size=kernel, strides=stride, activation='relu', padding='same')


def get_maxpool_layer(size):
    return MaxPooling2D(pool_size=(size, size), strides=size)


def get_dropout_layer(dropout):
    return Dropout(dropout)


def get_dense_layer(units):
    return Dense(activation="relu", units=units)


def get_fit_generator(classifier, trainingset, testset):
    class_weight = {0: 1.92,
                    1: 1.,
                    2: 2.24}
    return classifier.fit_generator(trainingset,
                                    class_weight=class_weight,
                                    epochs=epochs,
                                    validation_data=testset,
                                    validation_steps=test_size // batch_size)  # number of samples to use from validation generator at the end of every epoch.


def get_train_data_gen(train_datagen):
    return train_datagen.flow_from_directory('../../../images/dataset_1920x840/training',
                                             target_size=(image_size_y, image_size_x),
                                             batch_size=batch_size,
                                             class_mode='categorical')


def get_test_data_gen(test_datagen):
    return test_datagen.flow_from_directory('../../../images/dataset_1920x840/test',
                                            target_size=(image_size_y, image_size_x),
                                            batch_size=batch_size,
                                            class_mode='categorical')


def get_image_data_gen():
    return ImageDataGenerator(rescale=1. / 255,
                              rotation_range=40,
                              width_shift_range=0.2,
                              height_shift_range=0.2,
                              shear_range=0.2,
                              horizontal_flip=True)


def get_rescale_gen():
    return ImageDataGenerator(rescale=1. / 255)


def create_plot_acc(history, name):
    history_dict = history.history
    history_dict.keys()

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    epochs = range(1, len(acc) + 1)
    plt.clf()
    # "bo" is for "blue dot"
    plt.plot(epochs, acc, 'bo', label='Training accuracy')
    # b is for "solid blue line"
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)
    plt.legend()
    plt.savefig(name)


def create_plot_loss(history, name):
    history_dict = history.history
    history_dict.keys()

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(loss) + 1)
    plt.clf()
    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylim(top=5, bottom=0)
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(name)
