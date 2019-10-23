# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import backend as K
import matplotlib.pyplot as plt

# Initialising the CNN with the sequential model
classifier = Sequential()

# Step 1 - Convolution. Add a Convolution2D layer with 32 filters, 3x3 kernel size, 3 stride,
# input shape of image should be 64x64x3 and the activation function is relu, which makes all negative
# values in the matrix to zero.
classifier.add(Convolution2D(32, 3, 3, input_shape = (200, 112, 3), activation = 'relu'))

# Step 2 - Pooling. Adds a pooling layer with maxpooling, which only saves the max value into the
# new matrix
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(activation="relu", units=128))
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
                         samples_per_epoch = 8000,
                         nb_epoch = 3,
                         validation_data = test_set,
                         nb_val_samples = 2000)

history_dict = history.history
history_dict.keys()

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)
plt.clf()
# "bo" is for "blue dot"
plt.plot(epochs, loss, 'bo', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


# classifier.save('categoricalModel.h5')
K.clear_session()