from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
import numpy as np
from keras.preprocessing import image

classifier = load_model('binaryModel.h5')

# Load in image
image_paths = [
    'can22.jpg', 'can_23.jpg', 'can22.jpg'
]

for path in image_paths:
    test_image = image.load_img('../../files/images/test_set/waste/cans/' + path, target_size=(28, 28), color_mode='grayscale')
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict_proba(test_image)
    print(result[0])
