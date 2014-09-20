import movement
import direction
import heading

from helper import wrap_error


class BotError(Exception):
    pass


class InvalidMovement(BotError):
    pass


class Bot(object):
    def __init__(self):
        self._location = None
        self._facing = None

    @wrap_error((movement.OutOfBoundsError, heading.InvalidHeading),
                InvalidMovement)
    def place(self, loc, facing):
        new_loc = movement.jump_to(loc)
        new_facing = heading.face(facing)
        self._facing = heading.face(new_facing)
        self._location = movement.jump_to(new_loc)

    @wrap_error(heading.InvalidTurn, InvalidMovement)
    def turn_right(self):
        self._facing = heading.turn(direction.RIGHT, self._facing)

    @wrap_error(heading.InvalidTurn, InvalidMovement)
    def turn_left(self):
        self._facing = heading.turn(direction.LEFT, self._facing)

    @wrap_error(movement.OutOfBoundsError, InvalidMovement)
    def move(self):
        self._location = movement.move(self._facing, self._location)
