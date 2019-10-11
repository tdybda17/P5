from PIL import Image

from resizeimage import resizeimage

import os

for i in range(10):
    path = '/Volumes/BOOT/others' + str(i) + '/'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        if '/Volumes/BOOT/.Trashes' not in r:
            for file in f:
                if '.jpg' in file:
                    files.append(os.path.join(r, file))

    j = 0
    for file in files:
        with open(file, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [200, 200])
                filename = '/Volumes/BOOT/other_waste/w_' + str(i) + '_' + str(j) + '.jpg'
                cover.save(filename, image.format)
                j = j + 1
                print(filename + ' was saved')
