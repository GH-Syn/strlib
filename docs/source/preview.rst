Preview
=======

If you're just looking for a quick preview / overview of this library, here
are a few of my favorite bits and pieces.


Trim sentences
---------------

This function is useful for general syntax / grammar polish.
Note that you can also specify characters to ignore as well.

::

    sentence = "The quick brown fox .jumped over the lazy dog."
    formatted_sentence = strip_punctuation(sentence)
    print(formatted_sentence)

    >>> "The quick brown fox jumped over the lazy dog"

Decode URL strings
------------------

You can parse a URL as follows::

    import strlib

    url_string = strlib.parse_url("https%3A%2F%2Fgoogle%2Ecom")
    print(url_string)

    >>> "https://google.com"

Exclude characters from a URL
-----------------------------
You can also exclude characters if you wish::

    url_string = _parser.parse_url("https%3A%2F%2Fpython%2Eorg", ".")  # ...
    print(url_string)

    >>> "https://python%2Eorg"


