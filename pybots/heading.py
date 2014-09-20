import direction

from helper import wrap_error


class headings:
    """Collection of constants naming the valid headings"""
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


class InvalidHeading(Exception):
    pass


class InvalidTurn(Exception):
    pass


@wrap_error(KeyError, InvalidTurn)
def turn(dirn, head):
    """Return the heading resulting in turning `dirn` direction
    from `head` heading

    Raises:
        InvalidTurn -- when the turn or initial heading are not valid
    """
    return _neighbours[head][dirn]


def face(head):
    """Return the heading resulting in facing towards the `head` heading
    This is mostly useful for verifying a heading is valid.

    Raises:
        InvalidHeading -- when the heading is not valid
    """
    if head not in _neighbours:
        raise InvalidHeading()
    return head


_neighbours = {
    headings.NORTH: {
        direction.LEFT: headings.WEST,
        direction.RIGHT: headings.EAST
    },
    headings.EAST: {
        direction.LEFT: headings.NORTH,
        direction.RIGHT: headings.SOUTH
    },
    headings.SOUTH: {
        direction.LEFT: headings.EAST,
        direction.RIGHT: headings.WEST
    },
    headings.WEST: {
        direction.LEFT: headings.SOUTH,
        direction.RIGHT: headings.NORTH
    }
}
