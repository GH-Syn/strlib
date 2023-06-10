"""
Author: Joshua Rose <joshuarose099@gmail.com>

String operations and mutability functions for improvement to `re`.

`Exceptions are defined in ``_exceptions.py```
"""

import re
from ._decorators import prototype
from ._exceptions import InvalidCharacter


LITERALS = [
    ".",
    ",",
    "~",
    "`",
    "'",
    '"',
    "\\",
    "-",
    "=",
    "+",
    "&",
    "%",
    "$",
    "#",
    "!",
]
SYMBOLS = {
    "%21": "!",
    "%22": '"',
    "%23": "#",
    "%24": "$",
    "%25": "%",
    "%26": "&",
    "%27": "'",
    "%28": "(",
    "%29": ")",
    "%2A": "*",
    "%2B": "+",
    "%2C": ",",
    "%2D": "-",
    "%2E": ".",
    "%2F": "/",
    "%3A": ":",
    "%3B": ";",
    "%3C": "<",
    "%3D": "=",
    "%3E": ">",
    "%3F": "?",
    "%40": "@",
    "%5B": "[",
    "%5C": "\\",
    "%5D": "]",
    "%5E": "^",
    "%5F": "_",
    "%60": "`",
    "%7B": "{",
    "%7C": "|",
    "%7D": "}",
    "%7E": "~",
}


__all__ = ["LITERALS", "SYMBOLS", "convert_break_tags", "parse_url"]


def _is_char(_char):
    """Assert `char` is valid punctuation character."""

    return _char in LITERALS


def strip_punctuation(value, *chars):
    """Remove punctuation characters in `value`.

    >>> sentence = "The quick brown fox .jumped over the lazy dog."
    >>> strip_punctuation(sentence)
    >>> "The quick brown fox jumped over the lazy dog"
    """

    _literals = LITERALS.copy()
    value = list(value)

    if len(chars):
        for char in chars:
            if not _is_char(char):
                # NOTE code returns due to `InvalidCharacter`
                raise InvalidCharacter(
                    f"{char} is not a valid character literal"
                )

    for literal in _literals:
        if literal in value:
            value.remove(literal)

    return "".join(value)


def parse_url(url, **kwargs):
    """Parse url into an alpha-numeric string.

    Usage::

        url_string = _parser.parse_url(
                "https%3A%2F%2Fpython%2Eorg", exceptions="."
        )

        >>> "https://python%2Eorg"
    """

    exceptions = kwargs["exclude"] if len(kwargs) else []

    for symbol, replacement in SYMBOLS.items():
        if replacement not in exceptions:
            url = url.replace(symbol, replacement)

    return url


@prototype
def convert_break_tags(text, invert=False):
    r"""Parse html break tags into \n."""

    if "<br>" not in text:
        raise Warning("No <br> tags found in the text")

    text = re.sub("</br>", "", text)

    if invert:
        text = text.replace("<br>", "\n")
        text = text.replace("</br>", "")
        text = text.replace("\n", "<br>")
        return text.strip()

    text = text.replace("<br>", "\n")
    text = text.replace("<br>", "\n")

    return text.strip()
