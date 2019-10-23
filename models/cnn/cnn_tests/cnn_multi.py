# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import backend as K
from models.cnn.cnn_tests.customfunctions import getinitconvlayer, getconvlayer, getmaxpoollayer, getdropoutlayer, getdenselayer, createplot

# Initialising the CNN with the sequential model
classifier = Sequential()

# Step 1 - Convolution. Add a Convolution2D layer with 32 filters, 3x3 kernel size, 3 stride,
# input shape of image should be 64x64x3 and the activation function is relu, which makes all negative
# values in the matrix to zero.
classifier.add(getinitconvlayer(32, 3, 3))

# Step 2 - Pooling. Adds a pooling layer with maxpooling, which only saves the max value into the
# new matrix
classifier.add(getmaxpoollayer(2))

# Adding a second convolutional layer
classifier.add(getconvlayer(32, 3, 3))
classifier.add(getmaxpoollayer(2))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(getdenselayer(128))
classifier.add(Dense(activation="softmax", units=5))

# Compiling the CNN
classifier.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('../../files/images/dataset-resized/training_data',
                                                 target_size = (200, 112),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('../../files/images/dataset-resized/test_data',
                                            target_size = (200, 112),
                                            batch_size = 32,
                                            class_mode = 'categorical')

history = classifier.fit_generator(training_set,
                         samples_per_epoch = 100, #var 8000
                         nb_epoch = 1,
                         validation_data = test_set,
                         nb_val_samples = 2000)

createplot(history)


# classifier.save('categoricalModel.h5')
K.clear_session()