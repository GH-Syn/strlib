"""
Author: Joshua Rose <joshuarose099@gmail.com>

String operations and mutability functions for improvement to `re`.
"""

LITERALS = [".", ",", "~", "`", "\'", "\"", "\\",
             "-", "=", "+", "&", "%", "$", "#", "!"]

__all__ = ['LITERALS']

def _is_char(_char):
    """Assert `char` is valid punctuation character."""

    return _char in LITERALS

def _is_chars(*_chars):
    """Assert all chars are valid punctuation characters."""

    return all(char in LITERALS for char in _chars)

def strip_punctuation(value, *chars):
    """Remove punctuation characters in `value`.

     >>> sentence = "The quick brown fox .jumped over the lazy dog."
     >>> strip_punctuation(sentence)
     >>> "The quick brown fox jumped over the lazy dog"
    """

    _literals = LITERALS.copy()  # *slightly* faster 🚀

    if not _is_char(value) and not len(chars):
        # NOTE code returns due to `ValueError`
        raise PendingDeprecationWarning("{val} is not a valid punctuation character"
                         .format(val=value))

    if len(chars) and not _is_chars(chars):
        _literals.extend(chars)

    for literal in _literals:
        if literal in value:
            value.remove(literal)

    return value
