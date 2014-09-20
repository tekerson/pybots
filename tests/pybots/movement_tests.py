import pybots.movement as movement

import pybots.heading as heading

from nose.tools import assert_equals, raises


def test_move_north():
    [(yield check_move_north, x, y)
        for x in xrange(5)
        for y in xrange(4)]


def check_move_north(x, y):
    assert_equals(movement.move(heading.headings.NORTH, (x, y)), (x, y + 1))


def test_move_south():
    [(yield check_move_south, x, y)
        for x in xrange(5)
        for y in xrange(1, 5)]


def check_move_south(x, y):
    assert_equals(movement.move(heading.headings.SOUTH, (x, y)), (x, y - 1))


def test_move_east():
    [(yield check_move_east, x, y)
        for x in xrange(4)
        for y in xrange(5)]


def check_move_east(x, y):
    assert_equals(movement.move(heading.headings.EAST, (x, y)), (x + 1, y))


def test_move_west():
    [(yield check_move_west, x, y)
        for x in xrange(1, 5)
        for y in xrange(5)]


def check_move_west(x, y):
    assert_equals(movement.move(heading.headings.WEST, (x, y)), (x - 1, y))


def test_invalid_jump_to_raises_exception():
    [(yield check_invalid_jump_to_raises_exception, x, y)
        for x in (-1, 5)
        for y in (-1, 5)]


@raises(movement.OutOfBoundsError)
def check_invalid_jump_to_raises_exception(x, y):
    movement.jump_to((x, y))
