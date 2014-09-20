import pybots.cli as cli
import pybots.bot
import pybots.heading as heading


from nose.tools import assert_equals

unzip = lambda i: zip(*i)

cases = [
    [
        ("PLACE 0,0,NORTH", None),
        ("MOVE", None),
        ("REPORT", ((0, 1), heading.headings.NORTH))
    ],
    [
        ("PLACE 0,0,NORTH", None),
        ("LEFT", None),
        ("MOVE", pybots.bot.InvalidMovement),
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


def test_processor():
    for case in cases:
        i, o = unzip(case)
        check_processor(i, list(o))


def check_processor(lines, out):
    bot = pybots.bot.Bot()
    op = []

    process = cli.processor(
        bot,
        lambda o: op.append(o),
        lambda e: op.append(type(e))
    )

    for line in lines:
        process(line)
    assert_equals(op, out)
