import movement
import direction
import heading


class Bot(object):
    def __init__(self):
        self._location = None
        self._facing = None

    def place(self, loc, facing):
        try:
            new_loc = movement.jump_to(loc)
            new_facing = heading.face(facing)
        except movement.OutOfBoundsError, heading.InvalidHeading:
            raise InvalidMovement
        self._facing = heading.face(new_facing)
        self._location = movement.jump_to(new_loc)

    def turn_right(self):
        try:
            self._facing = heading.turn(direction.RIGHT, self._facing)
        except heading.InvalidTurn:
            raise InvalidMovement

    def turn_left(self):
        try:
            self._facing = heading.turn(direction.LEFT, self._facing)
        except heading.InvalidTurn:
            raise InvalidMovement

    def move(self):
        try:
            self._location = movement.move(self._facing, self._location)
        except movement.OutOfBoundsError:
            raise InvalidMovement


class InvalidMovement(Exception):
    pass
