import unittest

from .._exceptions import InvalidCharacter


class TestInvalidCharacter(unittest.TestCase):
    def test_dec_instance(self):
        # test declare instance of `InvalidCharacter`

        error = InvalidCharacter("test")

        self.assertIsInstance(error, InvalidCharacter)

    def test_raise_instance(self):
        error = InvalidCharacter("test")

        with self.assertRaises(InvalidCharacter):
            raise error
