from image_compressor.dir_walker.dir_walker import walk_dir
from image_compressor.image_comp import compress_image


source = '/Users/toby/Desktop/AllTestPictures/PlastikTest'
files = walk_dir(path=source, files_extensions=['.jpg', '.png', '.jpeg'])
i = 0
for file in files:
    filename = '/Users/toby/Desktop/TestBilleder/TestPlastik/plastic_' + str(i) + '_200x112.jpg'
    compress_image(file, dest_filename=filename, size=[200, 112])
    i = i + 1
