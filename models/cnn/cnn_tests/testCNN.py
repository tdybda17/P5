from keras.models import load_model
import numpy as np

classifier = load_model('categoricalModel.h5')

from keras.preprocessing import image

# Test cardboard image
np.set_printoptions(suppress=True)
test_image = image.load_img('testIMG/test_img_correct/papir1.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = test_image/255
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict_proba(test_image)


print(result[0])