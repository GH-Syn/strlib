"""
Author: Joshua Rose <joshuarose099@gmail.com>

`Custom exception classes for ``_parser.py```
"""


class InvalidCharacterError(Exception):
    def __init__(self, char):
        super().__init__(char)
        self.char = char
