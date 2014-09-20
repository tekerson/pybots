import pybots.heading as heading

import pybots.direction as direction

from nose.tools import assert_equals

turns = [(heading.SOUTH, heading.WEST),
         (heading.EAST, heading.SOUTH),
         (heading.NORTH, heading.EAST),
         (heading.WEST, heading.NORTH)]


def test_turn_right():
    for left, right in turns:
        assert_equals(heading.turn(direction.RIGHT, left), right)


def test_turn_left():
    for left, right in turns:
        assert_equals(heading.turn(direction.LEFT, right), left)
