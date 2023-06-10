"""
This module contains exception classes.
These classes are used to define errors
that aren't part of the standard library.
"""

from _typeshed import NoneType

class InvalidCharacter(Exception):
    char: str

    def __init__(self, char: str) -> NoneType:
        super().__init__(char)
        self.char = char
