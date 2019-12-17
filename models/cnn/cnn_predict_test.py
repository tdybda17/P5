from keras.models import load_model
import numpy as np
import os

classifier = load_model('models/cnn.h5')

from keras.preprocessing import image

resultarray = [0, 0, 0]

for filename in os.listdir('Glas'):
     np.set_printoptions(suppress=True)
     test_image = image.load_img('Glas/' + filename, target_size=(150, 150))
     test_image = image.img_to_array(test_image)
     test_image = test_image/255
     test_image = np.expand_dims(test_image, axis = 0)
     result = classifier.predict_proba(test_image)
     integer = max(result[0])
     for x in range(3):
          if result[0][x] == integer:
               resultarray[x] += 1

print(resultarray)