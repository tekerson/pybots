import sys

from helper import wrap_error

import bot
import command


def main(instream, outstream):
    process = processor(
        bot.Bot(),
        formatter(outstream)
    )
    for line in instream:
        process(line)


def processor(the_bot, output):
    def inner(line):
        try:
            cmd = command.parse(line.strip())
            out = cmd(the_bot)
            output(out)
        except (command.CommandError, bot.BotError):
            pass
    return inner


def formatter(outstream):
    def inner(output):
        if output is not None:
            (x, y), loc = output
            outstream.write("{},{},{}\n".format(x, y, loc))
    return inner


if __name__ == "__main__":
    main(sys.stdin, sys.stdout)
