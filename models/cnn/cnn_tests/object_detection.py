# import the Python Image processing Library

from PIL import Image
import numpy as np

# Create an Image object from an Image

imageObject = Image.open("../testIMG/frog.jpeg")


# Crop the iceberg portion
a = np.asarray(imageObject)

print(a[10,10])

cropped = imageObject.crop((100, 30, 400, 300))

# Display the cropped portion

cropped.show()