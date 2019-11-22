# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D, Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import backend as K
from models.cnn.cnn_tests.customfunctions import get_init_conv_layer, get_conv_layer, \
    get_maxpool_layer, get_dropout_layer, get_dense_layer, create_plot, get_fit_generator, \
    get_train_data_gen, get_test_data_gen, get_image_data_gen, get_rescale_gen
#dont work
# Initialising the CNN with the sequential model
classifier = Sequential()

# Convolution. Add a Convolution2D layer with 32 filters, 3x3 kernel size, 3 stride,
# input shape of image should be 64x64x3 and the activation function is ReLu, which makes all negative
# values in the matrix to zero.
classifier.add(get_init_conv_layer(64, 3, 1)) # ned til 198 x 110
classifier.add(get_conv_layer(64, 3, 1)) # ned til 97 x 53
classifier.add(get_maxpool_layer(2)) # ned til 99 x 55

classifier.add(get_conv_layer(128, 3, 1)) # ned til 97 x 53
classifier.add(get_conv_layer(128, 3, 1)) # ned til 97 x 53
classifier.add(get_maxpool_layer(2)) # ned til 48 x 26

classifier.add(get_conv_layer(256, 3, 1)) # ned til 97 x 53
classifier.add(get_conv_layer(256, 3, 1)) # ned til 97 x 53
classifier.add(get_maxpool_layer(2)) # ned til 48 x 26

# Flattening
classifier.add(Dropout(0.5))
classifier.add(Flatten())

# Full connection
classifier.add(get_dense_layer(1024))
classifier.add(get_dense_layer(1024))

classifier.add(Dense(activation="softmax", units=3))

# Compiling the CNN
classifier.compile(optimizer = 'Adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

train_datagen = get_image_data_gen()

test_datagen = get_rescale_gen()

training_set = get_train_data_gen(train_datagen)

test_set = get_test_data_gen(test_datagen)

history = get_fit_generator(classifier, training_set, test_set)
create_plot(history, 'model8')

# classifier.save('categoricalModeltest.h5')
K.clear_session()