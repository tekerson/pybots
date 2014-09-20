import heading


class CommandError(Exception):
    pass


class InvalidCommand(CommandError):
    pass


class InvalidArgument(CommandError):
    pass


def place(args):
    x, y, face = _parse_place_args(args)

    def do(bot):
        return bot.place((x, y), face)
    return do


def _parse_place_args(args):
    try:
        x, y, head = args.strip().split(",")
        return int(x), int(y), _parse_heading(head)
    except ValueError:
        raise InvalidArgument


def right(_):
    def do(bot):
        return bot.turn_right()
    return do


def left(_):
    def do(bot):
        return bot.turn_left()
    return do


def move(_):
    def do(bot):
        return bot.move()
    return do


_commands = {
    "RIGHT": right,
    "LEFT": left,
    "MOVE": move,
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
