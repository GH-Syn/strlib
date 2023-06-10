__all__ = ["prototype"]


def prototype(function, *args, **kwargs):
    """Mark a function as a work in progress.

    :raises NotImplementedError: When called at runtime.

    Usage::

        @deprecated("Use B instead")
        class A:
            pass

        @deprecated("Use g instead")
        def f():
            pass

        @overload
        @deprecated("int support is deprecated")
        def g(x: int) -> int: ...
        @overload
        def g(x: str) -> int: ...
    """

    def wrapper(*args, **kwargs):
        raise NotImplementedError("This function is not ready for production.")

    return wrapper
