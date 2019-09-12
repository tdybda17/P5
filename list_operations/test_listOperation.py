from unittest import TestCase

from list_operations.list_op import ListOperation


class TestListOperation(TestCase):
    def test_get(self):
        list = ['a', 'b', 'c']
        op = ListOperation(list)

        self.assertEqual(1, op.get('b'))

    def test_sort(self):
        list = ['y', 'a', 'g', 'm']
        op = ListOperation(list)

        self.assertEqual(['a', 'g', 'm', 'y'], op.sort())

    def test_another(self):
        str = "Tobias"
        self.assertTrue("as" in str)
