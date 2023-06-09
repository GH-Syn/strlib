_literals = [".", ",", "~", "`", "\'", "\"", "\\",
             "-", "=", "+", "&", "%", "$", "#", "!"]

def _is_char(_char):
    """Assert `char` is valid punctuation character."""
    return _char in _literals

def _is_chars(*_chars):
    """Assert all chars are valid punctuation characters."""
    return all(_char in _literals for char in _chars)

def strip_punctuation(value):
    """Remove punctuation characters in `value`.

     >>> sentence = "The quick brown fox .jumped over the lazy dog."
     >>> strip_punctuation(sentence)
     >>> "The quick brown fox jumped over the lazy dog"
    """
    if not _is_char(value):
        raise ValueError("{val} is not a valid punctuation character"
                         .format(val=value))

    # TODO ...
