import unittest

import os
import sys

sys.path.append(os.getcwd())

from ..strlib._exceptions import InvalidCharacter
from ..strlib import _parser
from ..strlib._parser import LITERALS as literals
from ..strlib._parser import convert_break_tags as parse_breaks


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
        text = "The quick fox."

        trimmed_text = _parser.strip_punctuation(text)

        assert trimmed_text == "The quick fox"


@unittest.skip("Skipping prototype tests")
class TestBreaks(unittest.TestCase):
    @unittest.skip("Skipping prototype function test_open_tag")
    def test_open_tag(self):
        text = "The<br>Quick<br>Fox"
        expected_result = "The\nQuick\nFox"

        result = parse_breaks(text)

        assert result == expected_result

    @unittest.skip("Skipping prototype function test_close_tag")
    def test_close_tag(self):
        text = "The<br></br>Quick<br></br>Fox"
        expected_result = "The\nQuick\nFox"

        result = parse_breaks(text)

        assert result == expected_result

    @unittest.skip("Skipping prototype function test_null_warn")
    def test_null_warn(self):
        with self.assertRaises(Warning):
            parse_breaks("The quick fox")

    @unittest.skip("Skipping prototype function test_warn_invert_tags")
    def test_warn_invert_tags(self):
        with self.assertRaises(Warning):
            parse_breaks("The quick fox", invert=True)


if __name__ == "__main__":
    unittest.main()
