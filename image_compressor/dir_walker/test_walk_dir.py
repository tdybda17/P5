from unittest import TestCase

from image_compressor.dir_walker.dir_walker import walk_dir


def check_equal_lists(l1, l2):
    return len(l1) == len(l2) and sorted(l1) == sorted(l2)


class TestWalkDir(TestCase):

    def test_walk_dir(self):
        dir = './'
        expected_files = [dir + '__init__.py', dir + 'dir_walker.py', dir + 'test_walk_dir.py']
        actual_files = walk_dir(dir, files_extensions=['.py'])
        self.assertTrue(check_equal_lists(expected_files, actual_files))
