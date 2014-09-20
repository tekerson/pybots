import heading


class CommandError(Exception):
    pass


class InvalidCommand(CommandError):
    pass


class InvalidArgument(CommandError):
    pass


def place(args):
    x, y, face = _parse_place_args(args)
    return lambda bot: bot.place((x, y), face)


def _parse_place_args(args):
    try:
        x, y, head = args.strip().split(",")
        return int(x), int(y), _parse_heading(head)
    except ValueError:
        raise InvalidArgument


_commands = {
    "RIGHT": lambda _: lambda bot: bot.turn_right(),
    "LEFT": lambda _: lambda bot: bot.turn_left(),
    "MOVE": lambda _: lambda bot: bot.move(),
    "PLACE": place
}


def parse(string):
    cmd, args = "".join([string, " "]).split(" ", 1)
    try:
        command = _commands[cmd]
    except KeyError:
        raise InvalidCommand
    return command(args)


_headings = {
    "NORTH": heading.headings.NORTH,
    "EAST": heading.headings.EAST,
    "SOUTH": heading.headings.SOUTH,
    "WEST": heading.headings.WEST
}


def _parse_heading(string):
    try:
        return _headings[string]
    except KeyError:
        raise InvalidArgument
