def wrap_error(catch, instead):
    def wrapper(f):
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except catch:
                raise instead
        return inner
    return wrapper
