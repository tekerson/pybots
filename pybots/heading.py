import direction

NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

neighbours = {
    NORTH: {
        direction.LEFT: WEST,
        direction.RIGHT: EAST
    },
    EAST: {
        direction.LEFT: NORTH,
        direction.RIGHT: SOUTH
    },
    SOUTH: {
        direction.LEFT: EAST,
        direction.RIGHT: WEST
    },
    WEST: {
        direction.LEFT: SOUTH,
        direction.RIGHT: NORTH
    }
}


def turn(direct, start):
    return neighbours[start][direct]
