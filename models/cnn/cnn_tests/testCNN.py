from keras.models import load_model
import numpy as np

classifier = load_model('Modeldeepenough.h5')

from keras.preprocessing import image

# Test cardboard image
for x in range(1):
    np.set_printoptions(suppress=True)
    test_image = image.load_img('../../../files/images/dataset-resized/dataset-resized/test_data/Glas/billede1.jpg', target_size=(190, 190))
    test_image = image.img_to_array(test_image)
    test_image = test_image/255
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict_proba(test_image)
    print(str(x) + "   ")
    print(result[0])

