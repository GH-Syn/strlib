import unittest

import _parser
from _parser import LITERALS as literals  # pyright: ignore


class TestParser(unittest.TestCase):
    def test__is_char(self):
        for literal in literals:
            assert _parser._is_char(literal)

    def test__is_chars(self):
        for literal in literals:
            self.subTest(_parser._is_chars(literal))

    def test_valid_literals(self):
        with self.assertRaises(PendingDeprecationWarning):
            _parser.strip_punctuation("a")
