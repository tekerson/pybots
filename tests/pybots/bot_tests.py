import pybots.bot as bot

from nose.tools import assert_equals


class TestBots(object):
    def __init__(self):
        self.bot = None

    def setup(self):
        self.bot = bot.Bot()

    def test_place_set_position(self):
        [(yield self.check_place_sets_position, x, y)
            for x in xrange(5)
            for y in xrange(5)]

    def check_place_sets_position(self, x, y):
        self.bot.place((x, y))
        assert_equals(self.bot._location, (x, y))
