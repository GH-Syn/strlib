_literals = [".", ",", "~", "`", "\'", "\"", "\\",
             "-", "=", "+", "&", "%", "$", "#", "!"]

def _is_char(_char):
    """Assert `char` is valid punctuation character."""

    return _char in _literals

def _is_chars(*_chars):
    """Assert all chars are valid punctuation characters."""

    return all(char in _literals for char in _chars)

def strip_punctuation(value, *chars):
    """Remove punctuation characters in `value`.

     >>> sentence = "The quick brown fox .jumped over the lazy dog."
     >>> strip_punctuation(sentence)
     >>> "The quick brown fox jumped over the lazy dog"
    """

    if len(chars) and not _is_chars(chars):
        raise ValueError("One or more chars aren\'t valid characters")
    elif not _is_char(value) and not len(chars):
        raise ValueError("{val} is not a valid punctuation character"
                         .format(val=value))

    for literal in _literals:
        if literal in value:
            value.remove(literal)

    return value
