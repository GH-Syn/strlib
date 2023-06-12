Functions
=========

.. py:function:: strlib.strip_punctuation(value, chars, ignore_terminal=False)
   :noindex:

   Remove punctuation characters from a string.

   Usage::

     >>> strip_punctuation("The quick brown fox .jumped over the lazy dog.", ".")
     >>> "The quick brown fox jumped over the lazy dog"

   With ``ignore_terminal`` keyword argument::

     >>> strip_punctuation("The quick brown fox! They jumped over the lazy dog.", ".", "!", ignore_terminal=True)
     >>> "The quick brown fox They jumped over the lazy dog!"

   :param value: Required string presumably containing punctuation
   :type value: str
   :param chars: Disregard selective punctuation characters
   :type chars: str
   :param ignore_terminal: Ignore end character, inclusive of chars parameter
   :type ignore_terminal: bool
   :raise InvalidCharacterError: If a character in chars is not punctual
   :return: A formatted version of `value` with punctuation removed.


.. py:function:: strlib.parse_url(url, kwargs)
   :noindex:

   Convert URL symbols into alphabetic notation.

   Usage::

     url_string = _parser.parse_url(
     "https%3A%2F%2Fpython%2Eorg", exceptions="."
     )

     >>> "https://python%2Eorg"

   :param url: Required URL string containing symbols
   :type url: str
   :param kwargs: Optional keyword arguments
   :return: A decoded URL string sourced from literals.


.. py:function:: strlib.lower_sentence(sentence)
   :noindex:

   Convert non-leading characters to lowercase.

   Usage::

     >>> _parser.lower_sentence("The quick Fox! Oh wow.")
     >>> "The quick fox! Oh wow."

   :param sentence: Required sentence value
   :type sentence: str
   :return: A formatted sentence

.. py:function:: strlib.insert_spacing(sentence)
   :noindex:

   Insert spacing breaks in front of punctuation characters::

   Usage::

      >>> insert_spacing("Test.Test.Test!")
      >>> "Test. Test. Test!"

   :param sentence: Required unformatted sentence value
   :type sentence: str
   :return: A formatted string with proper punctuation spacing

