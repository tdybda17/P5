from image_compressor.dir_walker.dir_walker import walk_dir
from image_compressor.image_comp import compress_image

__basedir__ = '/Users/toby/Desktop/'
# [0] should not end with '/' and [1] is the name of the source and [2] is the type i.e training or test
source_options = ['NyeBilleder/GlasTest', 'glas', 'test']

source = __basedir__ + source_options[0]
files = walk_dir(path=source, files_extensions=['.jpg', '.png', '.jpeg'])
i = 0
for file in files:
    filename = __basedir__ + source_options[2] + '_' + source_options[1] + '/' + source_options[1] + '_' + str(i) + '_200x112.jpg'
    compress_image(file, dest_filename=filename, size=[200, 112])
    print(filename + ' was created')
    i = i + 1

print('done')
