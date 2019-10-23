# import the Python Image processing Library

from PIL import Image
import numpy as np

# Create an Image object from an Image

imageObject = Image.open("../testIMG/car.jpg")

# Crop the iceberg portion

pix = np.array(imageObject)




cropped = imageObject.crop((100, 30, 400, 300))

# Display the cropped portion

cropped.show()