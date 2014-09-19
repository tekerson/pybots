import pybots.headings as headings

from nose.tools import assert_equals

turns = [("SOUTH", "WEST"),
         ("EAST", "SOUTH"),
         ("NORTH", "EAST"),
         ("WEST", "NORTH")]


def test_turn_right():
    for left, right in turns:
        assert_equals(headings.right_of(left), right)


def test_turn_left():
    for left, right in turns:
        assert_equals(headings.left_of(right), left)


def test_move_north():
    [(yield check_move_north, x, y)
        for x in xrange(5)
        for y in xrange(5)]


def check_move_north(x, y):
    assert_equals(headings.move("NORTH", (x, y)), (x, y + 1))


def test_move_south():
    [(yield check_move_south, x, y)
        for x in xrange(5)
        for y in xrange(5)]


def check_move_south(x, y):
    assert_equals(headings.move("SOUTH", (x, y)), (x, y - 1))


def test_move_east():
    [(yield check_move_east, x, y)
        for x in xrange(5)
        for y in xrange(5)]


def check_move_east(x, y):
    assert_equals(headings.move("EAST", (x, y)), (x + 1, y))


def test_move_west():
    [(yield check_move_west, x, y)
        for x in xrange(5)
        for y in xrange(5)]


def check_move_west(x, y):
    assert_equals(headings.move("WEST", (x, y)), (x - 1, y))
