import heading

from helper import wrap_error


class CommandError(Exception):
    """The parent Exception for all Exceptions raised by the command module"""
    pass


class InvalidCommand(CommandError):
    pass


class InvalidArgument(CommandError):
    pass


@wrap_error(KeyError, InvalidCommand)
def parse(string):
    """Parse the user provided command and return a command function
    to be targeted at a bot

    Arguments:
        string -- The user provided command string to parse
                  in "COMMAND ARGS" format where ARGS are command specific

    Raises:
        InvalidCommand -- on an unrecognised/malformed command
        InvalidArgument -- on unrecognised/malformed command argument(s)
    """
    cmd, args = "".join([string, " "]).split(" ", 1)
    command = _commands[cmd]
    return command(args)


def _place(args):
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
    "REPORT": lambda _: lambda bot: bot.report(),
    "PLACE": _place
}


_headings = {
    "NORTH": heading.headings.NORTH,
    "EAST": heading.headings.EAST,
    "SOUTH": heading.headings.SOUTH,
    "WEST": heading.headings.WEST
}


@wrap_error(KeyError, InvalidArgument)
def _parse_heading(string):
    return _headings[string]
