"""
Author: Joshua Rose <joshuarose099@gmail.com>

Types for _exceptions.py
"""

from _typeshed import NoneType

class InvalidCharacter(Exception):
    char: str

    def __init__(self, char: str) -> NoneType:
        super().__init__(char)
        self.char = char
