from _typeshed import AnyOrLiteralStr
from typing import Any

def prototype(
    function: object, *args: tuple[AnyOrLiteralStr], **kwargs: tuple[Any]
) -> function: ...
