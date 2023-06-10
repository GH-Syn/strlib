import unittest

import _parser
from _parser import LITERALS as literals  # pyright: ignore unknown import


class TestParser(unittest.TestCase):
    def test__is_char(self):
        for literal in literals:
            assert _parser._is_char(literal)

    def test__is_chars(self):
        for literal in literals:
            # NOTE deprecation warning is ignored via pyright
            self.subTest(_parser._is_chars(literal))  # pyright: ignore

    def test_valid_literals(self):
        with self.assertRaises(PendingDeprecationWarning):
            _parser.strip_punctuation("a")

    def test_url(self):
        url_string = _parser.parse_url("https%3A%2F%2Fgoogle%2Ecom")

        assert url_string == "https://google.com"

    def test_url_exclude(self):
        url_string = _parser.parse_url(
            "https%3A%2F%2Fpython%2Eorg", "."  # pyright: ignore
        )  # ...

        assert url_string == "https://python%2Eorg"
