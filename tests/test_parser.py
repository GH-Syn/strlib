import unittest

from _exceptions import InvalidCharacter
import _parser
from _parser import LITERALS as literals


class TestParser(unittest.TestCase):
    def test__is_char(self):
        for literal in literals:
            assert _parser._is_char(literal)

    def test_valid_literals(self):
        with self.assertRaises(InvalidCharacter):
            _parser.strip_punctuation("test", "nonchar")  # pyright: ignore

    def test_url(self):
        url_string = _parser.parse_url("https%3A%2F%2Fgoogle%2Ecom")

        assert url_string == "https://google.com"

    def test_url_exclude(self):
        url_string = _parser.parse_url(
            "https%3A%2F%2Fpython%2Eorg", exclude="."  # pyright: ignore
        )  # ...

        assert url_string == "https://python%2Eorg"

    def test_punctuation(self):
        text = "The brown fox."

        trimmed_text = _parser.strip_punctuation(text)

        assert trimmed_text == "The brown fox"
