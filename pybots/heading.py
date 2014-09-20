import pybots.direction as direction

class headings:
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

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

class InvalidHeading(Exception):
    pass

def turn(dirn, start):
    return neighbours[start][dirn]

def face(head):
    if not head in neighbours:
        raise InvalidHeading
    return head
