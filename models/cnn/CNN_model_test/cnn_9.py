# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import backend as K
from models.cnn.cnn_tests.customfunctions import getinitconvlayer, getconvlayer, \
    getmaxpoollayer, getdropoutlayer, getdenselayer, createplot, getfitgenerator, \
    gettraindatagen, gettestdatagen, getimagedatagen, getrescalegen

# Initialising the CNN with the sequential model
classifier = Sequential()

# Step 1 - Convolution. Add a Convolution2D layer with 32 filters, 3x3 kernel size, 3 stride,
# input shape of image should be 64x64x3 and the activation function is relu, which makes all negative
# values in the matrix to zero.
classifier.add(getinitconvlayer(64, 4, 1))
classifier.add(getconvlayer(64, 4, 1))

# Step 2 - Pooling. Adds a pooling layer with maxpooling, which only saves the max value into the
# new matrix
classifier.add(getmaxpoollayer(2))

# Adding a second convolutional layer
classifier.add(getconvlayer(128, 4, 1))
classifier.add(getconvlayer(128, 4, 1))
classifier.add(getmaxpoollayer(2))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(getdenselayer(256))
classifier.add(getdenselayer(128))
classifier.add(getdenselayer(64))
classifier.add(Dense(activation="softmax", units=3))

# Compiling the CNN
classifier.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images
train_datagen = getimagedatagen()

test_datagen = getrescalegen()

training_set = gettraindatagen(train_datagen)

test_set = gettestdatagen(test_datagen)

history = getfitgenerator(classifier, training_set, test_set)
createplot(history)


# classifier.save('categoricalModel.h5')
K.clear_session()