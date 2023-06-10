"""
Author: Joshua Rose <joshuarose099@gmail.com>

Types for _exceptions.py
"""

from _typeshed import NoneType

class InvalidCharacterError(Exception):
    """InvalidCharacterError raised when an invalid literal is parsed.

    This class is used to express a mismatched literal when being parsed in
    a function as either a regular character or as part of a URL.

    Args:
        char (str): Character literal raised from error

    """
    char: str

    def __init__(self, char: str) -> NoneType:
        super().__init__(char)
        self.char = char
