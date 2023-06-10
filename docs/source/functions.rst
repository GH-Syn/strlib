Functions
=========

.. py:function:: strlib.strip_punctuation(value, *chars)
   :noindex:

   Remove punctuation characters from a string.

   :param value: Required string presumably containing punctuation
   :type value: str
   :param chars: Disregard selective punctuation characters
   :type chars: str
   :raise InvalidCharacterError: If a character in chars is not punctual
   :return: A formatted version of `value` with punctuation removed.


.. py:function:: strlib.parse_url(url, **kwargs)
   :noindex:

   Convert URL symbols into alphabetic notation.

   :param url: Required URL string containing symbols
   :type url: str
   :param kwargs: Optional keyword arguments
   :return: A decoded URL string sourced from literals.

