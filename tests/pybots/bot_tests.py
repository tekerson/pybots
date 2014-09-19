import pybots.bot as bot

from nose.tools import assert_equals, raises


class TestBots(object):
    def __init__(self):
        self.bot = None

    def setup(self):
        self.bot = bot.Bot(5, 5)

    def test_place_set_position(self):
        [(yield self.check_place_sets_position, x, y)
            for x in xrange(5)
            for y in xrange(5)]

    def check_place_sets_position(self, x, y):
        self.bot.place(x, y)
        assert_equals(self.bot._location, (x, y))

    def test_invalid_place_raises_exception(self):
        [(yield self.check_invalid_place_raises_exception, x, y)
            for x in (-1, 5)
            for y in (-1, 5)]

    @raises(bot.OutOfBoundsError)
    def check_invalid_place_raises_exception(self, x, y):
        self.bot.place(x, y)
