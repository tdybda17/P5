# import the Python Image processing Library

from PIL import Image
import numpy as np

# Create an Image object from an Image

imageObject = Image.open("../../../files/images/dataset-resized/test_data/Batterier/aTest1.jpg")


# Crop the iceberg portion

cropped = imageObject.crop((0, 100, 1920, 1000))

arr = np.asarray(cropped)

print(arr[200, 200])

# Display the cropped portion

cropped.show()