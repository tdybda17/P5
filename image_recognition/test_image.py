from unittest import TestCase

from image_recognition.image import Image


class TestImage(TestCase):

    def test_my_method(self):
        self.assertTrue(1)

    def test_another_method(self):
        p = Image(3, 3)
        self.assertEqual(p.myMethod(2), 5)
