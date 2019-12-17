import cv2
from keras.models import load_model
import numpy as np
import os

classifier = load_model('../cnn.h5')

resultarray = [0, 0, 0]

for filename in os.listdir('../../images/test_set_cropped'):
     img = cv2.imread('../../images/test_set_cropped/Batteries' + filename, cv2.IMREAD_COLOR)
     test_image = cv2.resize(img, (150, 150), interpolation=cv2.INTER_AREA)
     test_image = test_image / 255
     test_image = np.expand_dims(test_image, axis=0)
     result = classifier.predict_proba(test_image)
     integer = max(result[0])
     for x in range(3):
          if result[0][x] == integer:
               resultarray[x] += 1
print('Batteries: ')
print(resultarray)

resultarray = [0, 0, 0]
for filename in os.listdir('../../images/test_set_cropped'):
     img = cv2.imread('../../images/test_set_cropped/Cans' + filename, cv2.IMREAD_COLOR)
     test_image = cv2.resize(img, (150, 150), interpolation=cv2.INTER_AREA)
     test_image = test_image / 255
     test_image = np.expand_dims(test_image, axis=0)
     result = classifier.predict_proba(test_image)
     integer = max(result[0])
     for x in range(3):
          if result[0][x] == integer:
               resultarray[x] += 1
print('Cans: ')
print(resultarray)

resultarray = [0, 0, 0]
for filename in os.listdir('../../images/test_set_cropped'):
     img = cv2.imread('../../images/test_set_cropped/Glas' + filename, cv2.IMREAD_COLOR)
     test_image = cv2.resize(img, (150, 150), interpolation=cv2.INTER_AREA)
     test_image = test_image / 255
     test_image = np.expand_dims(test_image, axis=0)
     result = classifier.predict_proba(test_image)
     integer = max(result[0])
     for x in range(3):
          if result[0][x] == integer:
               resultarray[x] += 1
print('Glas: ')
print(resultarray)
