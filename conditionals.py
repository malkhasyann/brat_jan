""" Brat jan! This is a module for conditionals. """

import sys

import expressions
import states
import errors
import validity
import bodies


def if_condition(index, line):
    splitted_line = line.split()

    if splitted_line[0] != 'if':
        errors.syntax_error()

    value = expressions.execute_expression(" ".join(splitted_line[1:]))
    if value:
        instructions = bodies.define_body(index, line)
        bodies.body(instructions)
