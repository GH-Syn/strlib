"""
Author: Joshua Rose <joshuarose099@gmail.com>

String operations and mutability functions for improvement to `re`.
"""

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


__all__ = ["LITERALS"]


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
        raise PendingDeprecationWarning(
            "{val} is not a valid punctuation character".format(val=value)
        )

    if len(chars) and not _is_chars(chars):
        _literals.extend(chars)

    for literal in _literals:
        if literal in value:
            value.remove(literal)

    return value


def parse_url(url, *_chars):
    """Parse url into an alpha-numeric string.

    :param *chars: characters to exclude.
    """

    decoded_url = "".join(
        SYMBOLS.get(char, char) for char in url if char not in _chars
    )

    return decoded_url
