import unittest

import os
import sys

sys.path.append(os.getcwd())

from ..strlib._exceptions import InvalidCharacterError


class TestInvalidCharacter(unittest.TestCase):
    def test_dec_instance(self):
        # test declare instance of `InvalidCharacter`

        error = InvalidCharacterError("test")

        self.assertIsInstance(error, InvalidCharacterError)

    def test_raise_instance(self):
        error = InvalidCharacterError("test")

        with self.assertRaises(InvalidCharacterError):
            raise error
