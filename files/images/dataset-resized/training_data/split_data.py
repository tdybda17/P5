import os
import random

files = os.listdir('Batterier/')
random.shuffle(files)
length = len(files)
test_size = length * 0.25

i = 0
for file in files:
    os.rename("Batterier/" + file, "../test_data/Batterier/" + file)
    i = i + 1
    if i > test_size:
        break