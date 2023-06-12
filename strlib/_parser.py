import re

from ._decorators import prototype
from ._exceptions import InvalidCharacterError


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


__all__ = [
    "LITERALS",
    "SYMBOLS",
    "convert_break_tags",
    "parse_url",
    "lower_sentence",
    "insert_spacing",
]


def _is_char(_char):
    """Assert `char` is valid punctuation character."""

    return _char in LITERALS


def insert_spacing(sentence):
    """Insert spacing breaks in front of punctuation characters.

    :param sentence: A string that is formatted - see example as shown above
    """

    _sentence = list(sentence)

    for index, word in enumerate(_sentence):
        if index < len(_sentence):
            if word == any(["!", ".", "?"]):
                if _sentence[index + 1] != " ":
                    _sentence.insert(index + 1, " ")


def lower_sentence(sentence):
    """Convert every character that isn't the start of a sentence to lowercase.

    :param sentence: Required string value with >= 2 words
    """

    _sentence = list(sentence)

    for index, letter in enumerate(_sentence):
        if index == 1:
            continue
        if index + 1 < len(_sentence) and letter.isalnum():
            if letter in ["!", ".", "?"]:
                # If there is a space after punctuation
                if _sentence[index + 1] == " ":
                    # Then capitalize the letter after it if it's a letter
                    if _sentence[index + 2].isalnum():
                        _sentence[index + 2] = _sentence[index - 2].upper()
                # If no space after punctuation, capitalize letter if alphanumeric
                elif _sentence[index + 1].isalnum():
                    _sentence[index + 1] = _sentence[index + 1].upper()
                # Otherwise convert it to lowercase
            elif _sentence[index - 2] in ["!", ".", "?"]:
                _sentence[index] = _sentence[index].upper()
            else:
                # This is just going to be punctuation ...
                _sentence[index] = _sentence[index].lower()

    # Minor tweaks
    if _sentence[1].isupper():
        _sentence[1] = _sentence[1].lower()
    if not _sentence[0].isupper():
        _sentence[0] = sentence[0].upper()

    return "".join(_sentence)


def strip_punctuation(value, *chars, ignore_terminal=False):
    """Remove punctuation characters from a string.

    :param value: Required string presumably containing punctuation
    :param terminal: Ignore ending character of value
    :return: String with punctuation removed.
    """

    _literals = LITERALS.copy()
    value = list(value)
    terminal = value[-1:]

    if ignore_terminal:
        value.pop(len(value) - 1)

    if len(chars):
        for char in chars:
            if not _is_char(char):
                # NOTE code returns due to `InvalidCharacter`
                raise InvalidCharacterError(
                    f"{char} is not a valid character literal"
                )

    for literal in _literals:
        if literal in value:
            value.remove(literal)

    if ignore_terminal:
        value.append(*terminal)

    return "".join(value)


def parse_url(url, **kwargs):
    """Parse url into an alpha-numeric string."""

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
