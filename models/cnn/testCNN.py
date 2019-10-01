from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
import numpy as np

classifier = load_model('model.h5')

from keras.preprocessing import image

# Category options
categories = {
    0: 'cardboard',
    1: 'glass',
    2: 'metal',
    3: 'paper',
    4: 'plastic'
}


def get_result(result_arr, categories_arr):
    index_of_result = result_arr.index(1)
    if index_of_result < len(categories_arr):
        return categories_arr[index_of_result]
    else:
        raise Exception('Index of result was higher can size of categories')


test_image = image.load_img('testIMG/cardboard281.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)

print(get_result(result[0], categories))
