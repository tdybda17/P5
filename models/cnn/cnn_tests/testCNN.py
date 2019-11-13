from keras.models import load_model
import numpy as np

classifier = load_model('categoricalModeltest.h5')

from keras.preprocessing import image

# Test cardboard image
for x in range(20):
    np.set_printoptions(suppress=True)
    test_image = image.load_img('../../../files/images/dataset-resized/test_data/Glas/glas_' + str(x) + '_200x112.jpg', target_size=(200, 112))
    test_image = image.img_to_array(test_image)
    test_image = test_image/255
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict_proba(test_image)
    print(str(x) + "   ")
    print(result[0])

