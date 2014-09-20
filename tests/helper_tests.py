import pybots.helper as helper

from nose.tools import assert_equals, raises


class MockInnerError(Exception):
    pass


class MockOuterError(Exception):
    pass


@raises(MockOuterError)
def test_wrap_error_helper_catches_and_raises_specified_errors():
    @helper.wrap_error(MockInnerError, MockOuterError)
    def f():
        raise MockInnerError()
    f()


def test_unzip():
    assert_equals(
        helper.unzip([(1, 2), (3, 4), (5, 6)]),
        [(1, 3, 5), (2, 4, 6)]
    )
    assert_equals(
        helper.unzip([(1, 2, 3), (4, 5, 6), (7, 8, 9)]),
        [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    )
