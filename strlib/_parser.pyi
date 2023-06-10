"""
Author: Joshua Rose <joshuarose099@gmail.com>

Types for _parser.py
"""

from _typeshed import AnyOrLiteralStr

LITERALS: list[str]
SYMBOLS: dict[str, str]
__all__: list[str]

def _is_char(_char: str) -> bool: ...
def strip_punctuation(value: str, *chars: tuple[str]) -> str: ...
def parse_url(url: str, **kwargs: dict[str, AnyOrLiteralStr]) -> str: ...
def convert_break_tags(string: str, invert: bool = False) -> str: ...
