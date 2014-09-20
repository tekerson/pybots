#!/usr/bin/env python

import sys

from helper import wrap_error

import bot
import command


def main(instream, outstream):
    process = processor(
        bot.Bot(),
        formatter(outstream),
        error(outstream)
    )
    for line in instream:
        process(line)


def processor(the_bot, output, error):
    def inner(line):
        try:
            cmd = command.parse(line.strip())
            out = cmd(the_bot)
            output(out)
        except (command.CommandError, bot.BotError) as e:
            error(e)
    return inner


def formatter(outstream):
    def inner(output):
        if output is not None and output is not Exception:
            (x, y), loc = output
            outstream.write("{},{},{}\n".format(x, y, loc))
    return inner


def error(outstream):
    def inner(output):
        pass
    return inner


if __name__ == "__main__":
    main(sys.stdin, sys.stdout)
