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

    if_instructions, if_next_index = bodies.define_body(index + 1)  # instructions, next code segment starting index

    else_instructions = None
    else_next_index = None

    final_index = if_next_index

    if states.source_code[if_next_index].startswith('else'):
        else_instructions, else_next_index = else_condition(if_next_index)
        final_index = else_next_index

    if value == 'True':
        bodies.body(if_instructions)
    elif else_instructions is not None:
        bodies.body(else_instructions)

    return final_index  # from where to continue execution on Global Loop


def else_condition(index):
    splitted_line = states.source_code[index].split()

    if splitted_line[0] != 'else':
        errors.syntax_error()

    body_code, next_index = bodies.define_body(index + 1)

    return body_code, next_index
