from PIL import Image

from resizeimage import resizeimage

import os

path = '/Users/toby/Desktop/dåser' + str(i) + '/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    if '/Users/toby/Desktop/dåser.Trashes' not in r:
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))

j = 0
for file in files:
    with open(file, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [112.5, 200])
            filename = '/Users/toby/Desktop/dåser_compressed/w_' + str(j) + '.jpg'
            cover.save(filename, image.format)
            j = j + 1
            print(filename + ' was saved')
