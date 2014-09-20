import pybots.direction as direction


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


def turn(dirn, head):
    try:
        return neighbours[head][dirn]
    except KeyError:
        raise InvalidTurn


def face(head):
    if head not in neighbours:
        raise InvalidHeading
    return head
