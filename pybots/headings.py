headings = [
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST",
]


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
