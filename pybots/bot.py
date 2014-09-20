import movement
import direction
import heading

from helper import wrap_error


class BotError(Exception):
    """The parent Exception for all Exceptions raised by the pybots.bot module"""
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
        """Place the bot in the specified `loc` (x, y), `facing` the given heading

        Arguments:
            loc -- the (x, y) location at which to place the bot
            facing -- the heading for the bot to face

        Raises:
            InvalidHeading -- if the heading isn't a valid value
            InvalidMovement -- if the placement would be out of bounds
        """
        new_loc = movement.jump_to(loc)
        new_facing = heading.face(facing)
        # perform the calculations before updating state so the update is
        # is consistent in the case of exceptions
        self._facing = heading.face(new_facing)
        self._location = movement.jump_to(new_loc)

    @wrap_error(heading.InvalidTurn, InvalidMovement)
    def turn_right(self):
        """Rotate the bot 90 degrees right.

        Raises:
            InvalidMovement -- if the bot can't be rotated
                               (ie. it hasn't been placed)
        """
        self._facing = heading.turn(direction.RIGHT, self._facing)

    @wrap_error(heading.InvalidTurn, InvalidMovement)
    def turn_left(self):
        """Rotate the bot 90 degrees left.

        Raises:
            InvalidMovement -- if the bot can't be rotated
                               (ie. it hasn't been placed)
        """
        self._facing = heading.turn(direction.LEFT, self._facing)

    @wrap_error(movement.OutOfBoundsError, InvalidMovement)
    def move(self):
        """Move the bot 1 space forward

        Raises:
            InvalidMovement -- if the bot can't be moved
                               (ie. it hasn't been placed or the move would
                               result in being out of bounds)
        """
        self._location = movement.move(self._facing, self._location)

    def report(self):
        """Return the location and heading of the bot. Both may be None if
        the bot has not been placed.
        """
        return self._location, self._facing
