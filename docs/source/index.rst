.. strlib documentation master file, created by
   sphinx-quickstart on Fri Jun  9 12:28:13 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

🥜 In a nutshell
================

Strlib removes the boilerplate and hundreds of utility functions, allowing you
to focus on what matters.

Trim sentences
----------------
::

    sentence = "The quick brown fox .jumped over the lazy dog."
    formatted_sentence = strip_punctuation(sentence)
    print(formatted_sentence)

    >>> "The quick brown fox jumped over the lazy dog"

Decode URL strings
--------------------
::

    import strlib

    url_string = strlib.parse_url("https%3A%2F%2Fgoogle%2Ecom")
    print(url_string)

    >>> "https://google.com"

Exclude characters from a URL
-------------------------------
::

    url_string = _parser.parse_url("https%3A%2F%2Fpython%2Eorg", ".")  # ...
    print(url_string)

    >>> "https://python%2Eorg"


📖 Contents
-----------

.. toctree::
    :maxdepth: 2

    faq

