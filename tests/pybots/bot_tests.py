import pybots.bot as bot
import pybots.heading as heading

from nose.tools import assert_equals, assert_true, raises


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
        self.bot.place((x, y), heading.headings.NORTH)
        assert_equals(self.bot._location, (x, y))

    def test_place_sets_facing(self):
        self.bot.place((0, 0), heading.headings.NORTH)
        assert_equals(self.bot._facing, heading.headings.NORTH)

    def test_move(self):
        self.bot.place((0, 0), heading.headings.NORTH)
        self.bot.move()
        assert_equals(self.bot._location, (0, 1))

    @raises(bot.InvalidMovement)
    def test_move_out_of_bounds_raises_invalid_move(self):
        self.bot.place((0, 0), heading.headings.SOUTH)
        self.bot.move()

    def test_move_out_of_bounds_doesnt_set_location(self):
        self.bot.place((0, 0), heading.headings.SOUTH)
        try:
            self.bot.move()
            assert_true(False, "Expected exception not raised")
        except bot.InvalidMovement:
            pass
        assert_equals(self.bot._location, (0, 0))

    def test_turn_right(self):
        self.bot.place((0, 0), heading.headings.NORTH)
        self.bot.turn_right()
        assert_equals(self.bot._facing, heading.headings.EAST)

    def test_turn_left(self):
        self.bot.place((0, 0), heading.headings.NORTH)
        self.bot.turn_left()
        assert_equals(self.bot._facing, heading.headings.WEST)

    @raises(bot.InvalidMovement)
    def test_place_out_of_bounds_raises_invalid_move(self):
        self.bot.place((-1, 0), heading.headings.NORTH)

    @raises(bot.InvalidMovement)
    def test_place_with_bad_heading_raises_invalid_move(self):
        self.bot.place((0, 0), "BACKWARDS")

    def test_place_with_bad_heading_doesnt_set_location_or_facing(self):
        try:
            self.bot.place((0, 0), "BACKWARDS")
            assert_true(False, "Expected exception not raised")
        except bot.InvalidMovement:
            pass
        assert_equals(self.bot._location, None)
        assert_equals(self.bot._facing, None)

    def test_place_out_of_bounds_doesnt_set_facing_or_location(self):
        try:
            self.bot.place((-1, 0), heading.headings.NORTH)
            assert_true(False, "Expected exception not raised")
        except bot.InvalidMovement:
            pass
        assert_equals(self.bot._facing, None)
        assert_equals(self.bot._location, None)
