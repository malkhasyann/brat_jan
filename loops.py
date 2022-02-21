""" Brat jan! This is a module for loops. """

import expressions
import states
import errors
import bodies


def while_execution(index, line):
    splitted_line = line.split()

    if splitted_line[0] != 'while':
        errors.syntax_error()

    condition = " ".join(splitted_line[1:])
    value = expressions.execute_expression(condition)

    while_instructions, while_next_index = bodies.define_body(index + 1)  # instructions, next segment starting index

    while value == 'True':
        bodies.body(while_instructions)
        value = expressions.execute_expression(condition)

    return while_next_index
