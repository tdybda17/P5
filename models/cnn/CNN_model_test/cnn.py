#Imports
from keras.models import Sequential
from keras.layers import Flatten
from keras import backend as K, optimizers
from models.cnn.cnn_tests.customfunctions import *

#Setting the names for the graph files and the model
graph_acc_name = "cnn_9_acc"
graph_loss_name = "cnn_9_loss"
model_name = "cnn_9.h5"

#Model is initialized
classifier = Sequential()

#Convolutional and max pooling layers are added to the model.
classifier.add(get_init_conv_layer(filters=64, kernel=3, stride=1))
classifier.add(get_maxpool_layer(size=2))

classifier.add(get_conv_layer(filters=128, kernel=3, stride=1))
classifier.add(get_maxpool_layer(size=2))

classifier.add(get_conv_layer(filters=256, kernel=3, stride=1))
classifier.add(get_maxpool_layer(size=2))

classifier.add(get_conv_layer(filters=512, kernel=3, stride=1))
classifier.add(get_maxpool_layer(size=2))

classifier.add(get_conv_layer(filters=512, kernel=3, stride=1))
classifier.add(get_maxpool_layer(size=2))

#A dropout and flatten layer are added to the model
classifier.add(Dropout(rate=0.5))
classifier.add(Flatten())

#Two dense layers are addded to the model, one with 2048 neurons and the other with 3.
#The last dense layer is the output layer, which should give a probability vector
classifier.add(get_dense_layer(units=2048))

classifier.add(Dense(activation="softmax", units=3))

#Learning rate is set
adam = optimizers.Adam(learning_rate=0.00025)

#The model is compiled and ready for training
classifier.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

#A training data generator is created that will augment the images
training_data_generator = get_image_data_generator()

#A validation data generator is created that will scale down the pixels of the validation images
validation_data_generator = get_validation_generator()

#Training and validation sets are both created with the generators, that use the original data sets to augment and generator images
training_set = get_training_data_generator(training_data_generator)

validation_set = get_validation_data_generator(validation_data_generator)

#Creates the training and validation accuracy and loss graphs and saves them. Also saves the model and clears the keras session
history = get_fit_generator(classifier, training_set, validation_set)
create_plot_acc(history, graph_acc_name)
create_plot_loss(history, graph_loss_name)

classifier.save(model_name)
K.clear_session()