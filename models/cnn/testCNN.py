from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
import numpy as np

classifier = load_model('model.h5')

from keras.preprocessing import image

# Test cardboard image

test_image = image.load_img('testIMG/cardboard281.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
if 1 in result[:, 0]:
    print("This was correctly cardboard")
else:
    print("This was incorrectly predicted")

# Test glass image
test_image = image.load_img('testIMG/glass326.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
if 1 in result[:, 1]:
    print("This was correctly glass")
else:
    print("This was incorrectly predicted")

# Test metal image
test_image = image.load_img('testIMG/metal333.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
if 1 in result[:, 2]:
    print("This was correctly metal")
else:
    print("This was incorrectly predicted")

# Test paper image
test_image = image.load_img('testIMG/paper223.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
if 1 in result[:, 3]:
    print("This was correctly paper")
else:
    print("This was incorrectly predicted")

# Test plastic image
test_image = image.load_img('testIMG/plastic313.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
if 1 in result[:, 4]:
    print("This was correctly plastic")
else:
    print("This was incorrectly predicted")

