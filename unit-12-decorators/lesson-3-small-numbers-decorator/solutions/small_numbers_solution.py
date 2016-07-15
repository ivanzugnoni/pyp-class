import numbers


def small_numbers(limit=50):
    def dec(fn):
        def wrapped(*args, **kwargs):
            for arg in args:
                if isinstance(arg, numbers.Number):
                    if arg > limit:
                        raise ValueError("Invalid Number")
            return fn(*args, **kwargs)
        return wrapped
    return dec
