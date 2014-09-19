headings = [
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST",
]


move_map = {
    "NORTH": (0, 1),
    "EAST": (1, 0),
    "SOUTH": (0, -1),
    "WEST": (-1, 0),
}


def right_of(start):
    pos = headings.index(start)
    try:
        return headings[pos + 1]
    except IndexError:
        return headings[0]


def left_of(start):
    pos = headings.index(start)
    try:
        return headings[pos - 1]
    except IndexError:
        return headings[0]


def move(heading, loc):
    return add_elementwise(loc, move_map[heading])


def add_elementwise(a, b):
    return tuple(sum(x) for x in zip(a,b))
