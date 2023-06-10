======
💡 FAQ
======


How is this library different from ``re``?
==========================================

While ``re`` has very powerful syntax, it's difficult to utilize if you're not
already familiar with the regular expression syntax. This library minimizes
the prerequisite knowledge to utilize re, and, in fully plain English, gives
the user what ``re`` lacks in comprehensiveness.

For example, ``strlib`` is great at handling URL formats. You *could* use `re`,
``urllib``, or ``strlib``. Let me explain why the former would suit most cases.

In ``re``, you could do something like the following::

    import re

    url = "https%3A%2F%2Fgoogle%2Ecom"
    re.sub('%([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), url)

    >>> "https://google.com"

In ``urllib``, you'd do something simpler::

    from urllib.parse import urlparse

    urlparse("https%3A%2F%2Fgoogle%2Ecom")

    >>> "https://google.com"

The true power of ``strlib`` comes with its ability to handle uncommon edge cases.

For example, say you wanted to decode everything *but* a full-stop character.

``strlib`` makes this very straightforward::

    import strlib

    url = "https%3A%2F%2Fgoogle%2Ecom"
    strlib.parse_url(url, exclude=".")

    >>> "https://google%2Ecom"

What benefit does this library give?
====================================

This library is an expanse of many functions I find myself writing due to not
enough support or customizability from existing libraries. This library hopes
to give both the boilerplate and the mutability to the user, therefore eliminating
mental and physical overhead having to write out string utility functions.
This library will hopefully grow over time, as I add more to it.

Does this library even work?
============================
It's always a good idea to ask these sorts of questions before using a library.
Especially when the library isn't very popular. To give an idea of if this library
works or not, I invite you to look at the code coverage.
