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
