def wrap_error(catch, instead):
    def wrapper(f):
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except catch as inner:
                raise instead()
        return inner
    return wrapper

unzip = lambda i: zip(*i)
