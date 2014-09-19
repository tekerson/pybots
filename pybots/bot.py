class OutOfBoundsError(Exception):
    pass


class Bot(object):
    def __init__(self, max_x, max_y):
        self._max_x = max_x
        self._max_y = max_y
        self._location = None
        self._direction = None

    def place(self, x, y):
        self._assertInBounds(x, y)
        self._location = (x, y)

    def _assertInBounds(self, x, y):
        invalid_x = not 0 <= x < self._max_x
        invalid_y = not 0 <= y < self._max_y
        if (invalid_x or invalid_y):
            raise OutOfBoundsError()
