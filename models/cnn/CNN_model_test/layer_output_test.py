import os
import numpy as np
import matplotlib.pyplot as plt

from keras import models
from keras.preprocessing import image

model = models.load_model('Model7.h5')

np.set_printoptions(suppress=True)
img = image.load_img('../../../files/images/dataset-resized/dataset-resized/test_data/Dåser/can1_31_200x112.jpg', target_size=(150, 150))
test_image = image.img_to_array(img)
test_image = test_image/255
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict_proba(test_image)

print(result[0])



layer_outputs = [layer.output for layer in model.layers[:12]]
activation_model = models.Model(inputs = model.input, outputs = layer_outputs)
activations = activation_model.predict(test_image)

layer_names = []
for layer in model.layers[:12]:
    layer_names.append(layer.name)

images_per_row = 16

for layer_name, layer_activation in zip(layer_names, activations):
    n_features = layer_activation.shape[-1]

    size = layer_activation.shape[1]

    n_cols = n_features // images_per_row
    display_grid = np.zeros((size * n_cols, images_per_row * size))

    for col in range(n_cols):
        for row in range(images_per_row):
            channel_image = layer_activation[0, :, :, col * images_per_row + row]
            # Normalize tensors
            channel_image -= channel_image.mean()
            channel_image /= channel_image.std()
            channel_image *= 64
            channel_image += 128
            channel_image = np.clip(channel_image, 0, 255).astype('uint8')
            display_grid[col * size: (col + 1) * size,
            row * size: (row + 1) * size] = channel_image

    scale = 1. / size
    plt.figure(figsize=(scale * display_grid.shape[1],
                        scale * display_grid.shape[0]))

    plt.title(layer_name)
    plt.grid(False)
    plt.imshow(display_grid, aspect='auto', cmap='viridis')
    plt.show()


