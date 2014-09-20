import pybots.heading as heading

min_x, min_y = (0, 0)
max_x, max_y = (5, 5)

movements = {
    heading.NORTH: (0, 1),
    heading.EAST: (1, 0),
    heading.SOUTH: (0, -1),
    heading.WEST: (-1, 0),
}


class OutOfBoundsError(Exception):
    pass


def move(head, loc):
    dest = _zip_with(sum, loc, movements[head])
    return _assertInBounds(dest)


def jump_to(loc):
    return _assertInBounds(loc)


def _assertInBounds((x, y)):
    invalid_x = not min_x <= x < max_x
    invalid_y = not min_y <= y < max_y
    if (invalid_x or invalid_y):
        raise OutOfBoundsError()
    return (x, y)


def _zip_with(f, a, b):
    return tuple(f(x) for x in zip(a, b))
