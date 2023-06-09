import unittest
import _parser

from _parser import _literals as literals

_literals = [".", ",", "~", "`", "\'", "\"", "\\",
             "-", "=", "+", "&", "%", "$", "#", "!"]

class TestParser(unittest.TestCase):
    def test__is_char(self):
        for literal in literals:
            with self.subTest(isinstance(literal, str)==True):
                self.assertIn(literal, literals);

    def test_valid_literals(self):
        with self.assertRaises(ValueError):
            _parser.strip_punctuation("a")


