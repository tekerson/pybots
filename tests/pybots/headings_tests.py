import pybots.heading as heading

import pybots.direction as direction

from nose.tools import assert_equals

turns = [(heading.headings.SOUTH, heading.headings.WEST),
         (heading.headings.EAST, heading.headings.SOUTH),
         (heading.headings.NORTH, heading.headings.EAST),
         (heading.headings.WEST, heading.headings.NORTH)]


def test_turn_right():
    for left, right in turns:
        assert_equals(heading.turn(direction.RIGHT, left), right)


def test_turn_left():
    for left, right in turns:
        assert_equals(heading.turn(direction.LEFT, right), left)
