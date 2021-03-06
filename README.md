# pybots

## Requirements

Python: 2.7

Nose: 1.3 (for tests)

## What does it do?

Simulates a robot following commands to move around a virtual space. It reads a set of commands from standard input, follows the command tracking its location within the arena and ignoring invalid inputs.

## Usage

The primary executable is in the `bin` directory, it reads from standard input and writes to standard output.
If `python` is not on your path, you may need to pass `pybots/cli.py` to the interpreter manually.
Their are example input sequences in the `examples` directory.

To run `example1`, redirect stdin like so:

    bin/pybots < examples/example1

This should parse the commands and return and output the terminal. Other examples (`examples/example2` and `examples/example3`) are also available.


## Tests

A full (read: excessive) [nose](http://readthedocs.org/docs/nose/en/latest/) test suite is included in the `tests` directory. It can be run with the `nosetests` test runner from the project root.
