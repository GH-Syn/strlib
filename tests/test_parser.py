import os
import sys
import unittest

from ..strlib import _parser
from ..strlib._exceptions import InvalidCharacterError
from ..strlib._parser import LITERALS as literals
from ..strlib._parser import convert_break_tags as parse_breaks

sys.path.append(os.getcwd())




class TestParser(unittest.TestCase):
    def test__is_char(self):
        for literal in literals:
            assert _parser._is_char(literal)

    def test_valid_literals(self):
        with self.assertRaises(InvalidCharacterError):
            _parser.strip_punctuation("test", "nonchar")  # pyright: ignore

    def test_chars(self):
        _parser.strip_punctuation("test", ".")  # pyright: ignore

    def test_terminal(self):
        value = _parser.strip_punctuation(".test.", ".", ignore_terminal=False)

        assert value == "test."

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

    def test_lower_sentence(self):
        text = "The quick Fox! Oh wow."

        result = _parser.lower_sentence(text)

        assert result == "The quick fox! Oh wow."


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
