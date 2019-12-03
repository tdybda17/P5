from keras.models import Sequential
from keras.layers import Convolution2D, Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import backend as K, optimizers
from models.cnn.cnn_tests.customfunctions import get_init_conv_layer, get_conv_layer, \
    get_maxpool_layer, get_dropout_layer, get_dense_layer, create_plot_acc, create_plot_loss, get_fit_generator, \
    get_train_data_gen, get_test_data_gen, get_image_data_gen, get_rescale_gen

graph_acc_name = "cnn_18_acc"
graph_loss_name = "cnn_18_loss"
model_name = "cnn_18.h5"

classifier = Sequential()

classifier.add(get_init_conv_layer(64, 3, 1))
classifier.add(get_maxpool_layer(2))

classifier.add(get_conv_layer(128, 3, 1))
classifier.add(get_maxpool_layer(2))

classifier.add(get_conv_layer(256, 3, 1))
classifier.add(get_maxpool_layer(2))

classifier.add(get_conv_layer(512, 3, 1))
classifier.add(get_maxpool_layer(2))

classifier.add(get_conv_layer(512, 3, 1))
classifier.add(get_maxpool_layer(2))

classifier.add(Dropout(0.6))
classifier.add(Flatten())

classifier.add(get_dense_layer(2048))

classifier.add(Dense(activation="softmax", units=3))
adam = optimizers.Adam(learning_rate=0.00025)
classifier.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = get_image_data_gen()

test_datagen = get_rescale_gen()

training_set = get_train_data_gen(train_datagen)

test_set = get_test_data_gen(test_datagen)

history = get_fit_generator(classifier, training_set, test_set)
create_plot_acc(history, graph_acc_name)
create_plot_loss(history, graph_loss_name)

# classifier.save(model_name)
K.clear_session()
