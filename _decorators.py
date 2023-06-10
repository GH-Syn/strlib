__all__ = ["prototype"]


def prototype(function, *args, **kwargs):
    """Mark a function as a work in progress.

    :raises NotImplementedError: When called at runtime.
    """

    def wrapper(*args, **kwargs):
        raise NotImplementedError("This function is not ready for production.")

    return wrapper
