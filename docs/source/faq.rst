Purpose
=======

The purpose of this library is to provide a wide range of functions that
address the author's specific needs, which are not adequately met by existing libraries.

The motivation behind creating this library was the difficulty faced in organizing
and documenting numerous utility functions during the initial stages of developing the 'urban' project.
The goal of this library is to reduce the burden of utility functions by offering modularized formatting utilities and handling boilerplate code,
while also allowing for flexibility and reducing the mental and physical effort required to write string utility functions.

What distinguishes this library from others?
--------------------------------------------

While the re library offers powerful syntax for regular expressions, it can be challenging to utilize if you are not already familiar with its syntax.
This library aims to minimize the prerequisite knowledge required to work with regular expressions and provides a more comprehensive solution in plain English.

One notable advantage of this library is its proficiency in handling URL formats.
Although you have the option to use re, ``urllib``, or ``strlib`` for this purpose, let me elaborate on why the former is often the preferred choice.

With ``re``, you would typically perform the following steps::

    import re

    url = "https%3A%2F%2Fgoogle%2Ecom"
    re.sub('%([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), url)

    >>> "https://google.com"

On the other hand, ``urllib`` provides a simpler alternative::

    from urllib.parse import urlparse

    urlparse("https%3A%2F%2Fgoogle%2Ecom")

    >>> "https://google.com"

However, the true strength of this library lies in its capability to handle uncommon edge cases.
For instance, let's consider a scenario where you need to decode everything in a URL except for the period character.
In such cases, ``strlib`` simplifies the process significantly::

    import strlib

    url = "https%3A%2F%2Fgoogle%2Ecom"
    strlib.parse_url(url, exclude=".")

    >>> "https://google%2Ecom"

By leveraging the features provided by ``strlib``, you can handle such complex tasks with ease and clarity.
But if you're just looking for a quick preview / overview of this library, here
are a few of my favorite bits and pieces.

Trim sentences
---------------

This function is useful for general syntax / grammar polish::

    >>> strlib.strip_punctuation("The quick brown fox .jumped over the lazy dog.")
    >>> "The quick brown fox jumped over the lazy dog"


.. Note:: You can also specify characters to ignore as well as follows::

    >>> strlib.strip_punctuation("My toe... oh #!@$%*", ".")
    >>> "My toe oh #!@$%*"


Decode URL strings
------------------

You can parse a URL::

    >>> strlib.parse_url("https%3A%2F%2Fgoogle%2Ecom")
    >>> "https://google.com"

.. Note:: You can also exclude characters::

    >>> strlib.parse_url("https%3A%2F%2Fpython%2Eorg", ".")
    >>> "https://python%2Eorg"


