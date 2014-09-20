import pybots.cli as cli
import pybots.bot as bot
import pybots.heading as heading

from pybots.helper import unzip

from nose.tools import assert_equals

cases = [
    [
        ("PLACE 0,0,NORTH", None),
        ("MOVE", None),
        ("REPORT", ((0, 1), heading.headings.NORTH))
    ],
    [
        ("PLACE 0,0,NORTH", None),
        ("LEFT", None),
        ("MOVE", bot.InvalidMovement),
        ("REPORT", ((0, 0), heading.headings.WEST))
    ],
    [
        ("PLACE 1,2,EAST", None),
        ("MOVE", None),
        ("MOVE", None),
        ("LEFT", None),
        ("MOVE", None),
        ("REPORT", ((3, 3), heading.headings.NORTH))
    ]
]


def test_run():
    for case in cases:
        i, o = unzip(case)
        check_run(i, list(o))


def check_run(commands, out):
    op = []

    cli.run(commands, cli._process(
        bot.Bot(),
        lambda o: op.append(o),
        lambda e: op.append(type(e))
    ))

    assert_equals(op, out)
