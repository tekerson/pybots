import pybots.command as command
import pybots.heading as heading
import pybots.direction as direction

from nose.tools import assert_true, raises


def test_parsing_right_command_should_return_a_function():
    assert_true(callable(command.parse("RIGHT")))


def test_parsing_left_command_should_return_a_function():
    assert_true(callable(command.parse("LEFT")))


def test_parsing_move_command_should_return_a_function():
    assert_true(callable(command.parse("MOVE")))


def test_parsing_place_command_should_return_a_function():
    assert_true(callable(command.parse("PLACE 0,0,NORTH")))


def test_parsing_report_command_should_return_a_function():
    assert_true(callable(command.parse("REPORT")))


@raises(command.InvalidArgument)
def test_parsing_place_command_with_no_arguments_should_raise_invalid_argument():
    assert_true(callable(command.parse("PLACE")))


@raises(command.InvalidArgument)
def test_parsing_place_command_with_bad_heading_should_raise_invalid_argument():
    assert_true(callable(command.parse("PLACE 0,0,HOME")))


@raises(command.InvalidCommand)
def test_parsing_invalid_command_raises_invalid_command():
    assert_true(callable(command.parse("DANCE")))
