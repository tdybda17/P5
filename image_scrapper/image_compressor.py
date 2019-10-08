from PIL import Image

from resizeimage import resizeimage

import os

path = '/Volumes/BOOT/alu-soda-can/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    if '/Volumes/BOOT/.Trashes' not in r:
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))

i = 0
for file in files:
    with open(file, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [200, 200])
            filename = '/Volumes/BOOT/200x200-cans/can_1_' + str(i) + '.jpg'
            cover.save(filename, image.format)
            i = i + 1
            print(filename + ' was saved')
