"""
Decorators that aren't already part of builtin python type libraries are listed here.

Usage
=====

>>> @prototype("not ready yet 🤫")
>>> def foo():
>>>     return True

"""

from _typeshed import AnyOrLiteralStr
from typing import Any

def prototype(
    function: object, *args: tuple[AnyOrLiteralStr], **kwargs: tuple[Any]
) -> function: ...
