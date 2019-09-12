from matplotlib import pyplot as plt, cm
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

example_file = glob.glob('/Users/toby/PycharmProjects/P5/files/images/img1.png')[0]
im = imread(example_file, as_gray=True)

blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=0.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
num_rows = len(blobs_log)
print(num_rows)

# showing the image
fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r + 5, color='blue', linewidth=1, fill=False)
    print(c)
    ax.add_patch(c)

plt.show()

