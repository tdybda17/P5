import time

from image_compressor.dir_walker.dir_walker import walk_dir
from image_compressor.image_comp import compress_image


def get_time():
    return int(round(time.time() * 1000))


def write_to_file(times):
    f = open('/Users/toby/Desktop/results.txt', 'w')
    f.write('start_time_ms,end_time_ms,diff_ms\n')
    for time in times:
        f.write(str(time[0]) + ',')
        f.write(str(time[1]) + ',')
        f.write(str(time[1] - time[0]))
        f.write('\n')


__basedir__ = '/Users/toby/Desktop/'
source = __basedir__ + 'old'  # Name of source dir
dest_dir = 'new'  # Name of destination dir
files = walk_dir(path=source, files_extensions=['.jpg', '.png', '.jpeg'])
time_differences = []
i = 1
for file in files:
    filename = __basedir__ + dest_dir + '/' + 'test_glas_' + str(i) + '_1920x840.jpg'
    time_start = get_time()
    compress_image(file, dest_filename=filename, size=[1920, 840])
    time_end = get_time()
    time_differences.append([time_start, time_end])
    i += 1
    print(str(i) + ' of ' + str(len(files)))

write_to_file(time_differences)


