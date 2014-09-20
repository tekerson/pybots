import direction

from helper import wrap_error


class headings:
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


class InvalidHeading(Exception):
    pass


class InvalidTurn(Exception):
    pass


neighbours = {
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


@wrap_error(KeyError, InvalidTurn)
def turn(dirn, head):
    return neighbours[head][dirn]


def face(head):
    if head not in neighbours:
        raise InvalidHeading()
    return head
