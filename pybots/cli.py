#!/usr/bin/env python

import sys

from helper import wrap_error

import bot
import command
import heading


def run(commands, process):
    """Read the command stream and pass each command to be processed."""
    for command in commands:
        process(command)


def _process(the_bot, output, error):
    def inner(line):
        try:
            cmd = command.parse(line.strip())
            out = cmd(the_bot)
            output(out)
        except (command.CommandError, bot.BotError) as e:
            error(e)
    return inner


def _render_output(outstream):
    _headings = {
        heading.headings.NORTH: "NORTH",
        heading.headings.EAST: "EAST",
        heading.headings.SOUTH: "SOUTH",
        heading.headings.WEST: "WEST"
    }

    def inner(output):
        if output is not None and output is not Exception:
            (x, y), face = output
            outstream.write("{x},{y},{face}\n".format(
                x=x,
                y=y,
                face=_headings[face]
            ))
    return inner


def _handle_error(outstream):
    def inner(output):
        pass
    return inner


if __name__ == "__main__":
    run(sys.stdin, _process(
        bot.Bot(),
        _render_output(sys.stdout),
        _handle_error(sys.stdout)
    ))
