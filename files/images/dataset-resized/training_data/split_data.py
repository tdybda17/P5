import os
import random

files = os.listdir('../test_data/Batterier/')
random.shuffle(files)
length = len(files)
test_size = length * 0.16

i = 0
for file in files:
    os.rename("../test_data/Batterier/" + file, "Batterier/" + file)
    i = i + 1
    if i > test_size:
        break