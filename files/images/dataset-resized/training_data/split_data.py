import os
import random

files = os.listdir('Glas/')
random.shuffle(files)
length = len(files)
test_size = length * 0.16

i = 0
for file in files:
    os.rename("Glas/" + file, "../test_data/Glas/" + file)
    i = i + 1
    if i > test_size:
        break