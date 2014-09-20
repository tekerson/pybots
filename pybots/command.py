import heading

from helper import wrap_error


class CommandError(Exception):
    pass


class InvalidCommand(CommandError):
    pass


class InvalidArgument(CommandError):
    pass


def place(args):
    x, y, face = _parse_place_args(args)
    return lambda bot: bot.place((x, y), face)


@wrap_error(ValueError, InvalidArgument)
def _parse_place_args(args):
    x, y, head = args.strip().split(",")
    return int(x), int(y), _parse_heading(head)


_commands = {
    "RIGHT": lambda _: lambda bot: bot.turn_right(),
    "LEFT": lambda _: lambda bot: bot.turn_left(),
    "MOVE": lambda _: lambda bot: bot.move(),
    "PLACE": place
}


@wrap_error(KeyError, InvalidCommand)
def parse(string):
    cmd, args = "".join([string, " "]).split(" ", 1)
    command = _commands[cmd]
    return command(args)


_headings = {
    "NORTH": heading.headings.NORTH,
    "EAST": heading.headings.EAST,
    "SOUTH": heading.headings.SOUTH,
    "WEST": heading.headings.WEST
}


@wrap_error(KeyError, InvalidArgument)
def _parse_heading(string):
    return _headings[string]
