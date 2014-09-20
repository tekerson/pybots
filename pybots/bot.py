import movement


class Bot(object):
    def __init__(self):
        self._location = None
        self._facing = None

    def place(self, loc):
        self._location = movement.jump_to(loc)
