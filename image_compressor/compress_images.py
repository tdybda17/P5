import time

from image_compressor.dir_walker.dir_walker import walk_dir
from image_compressor.image_comp import compress_image


def get_time():
    return int(round(time.time() * 1000))


__basedir__ = '/Users/toby/Desktop/'
source = __basedir__ + 'old'  # Name of source dir
dest_dir = 'new'  # Name of destination dir
files = walk_dir(path=source, files_extensions=['.jpg', '.png', '.jpeg'])
time_differences = []
for file in files:
    time_start = get_time()
    filename = __basedir__ + dest_dir + '/' + 'glass_200x100.jpg'
    compress_image(file, dest_filename=filename, size=[200, 100])
    time_end = get_time()
    time_differences.append([time_start, time_end])
    break

print(time_differences)


