import pybots.command as cmd
import pybots.bot


from nose.tools import assert_equals


def test_basic():
    bot = pybots.bot.Bot()
    cmd.parse("PLACE 0,0,NORTH")(bot)
    cmd.parse("MOVE")(bot)
    assert_equals(bot._location, (0, 1))

