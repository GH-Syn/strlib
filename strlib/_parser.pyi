"""
This module contains various utility functions.
These functions help modify mutable string types.

Usage
=======
>>> strip_punctuation("Hi! 👋")
>>> "Hi 👋"  # Removes '!' punctuation character
"""

from _typeshed import AnyOrLiteralStr

LITERALS: list[str]
SYMBOLS: dict[str, str]
__all__: list[str]

def _is_char(_char: str) -> bool: ...
def strip_punctuation(
    value: str, *chars: str, ignore_terminal: bool = False
) -> str: ...
def parse_url(url: str, **kwargs: dict[str, AnyOrLiteralStr]) -> str: ...
def convert_break_tags(string: str, invert: bool = False) -> str: ...
def lower_sentence(sentence: str) -> str: ...
