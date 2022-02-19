""" Brat jan! This is a module for a print function. """

import errors
import expressions


def execute_bratwrite(instruction: str):
    if not instruction.startswith('bratwrite'):
        errors.syntax_error()

    expr = instruction  # copy the instruction
    expr = expr.replace('bratwrite', '', 1)  # remove substring 'bratwrite'
    expr = expressions.replace_var_name_by_value(expr)

    expr = str(eval(expr))  # execute the expression
    print(expr)


def check_parentheses(s: str):
    """ Brat jan! Checks whether parentheses are putted properly.
        Arguments:
            s -> text to check : str
    """
    pt_list = []  # parentheses history list
    for i in s:
        if i == '(':
            pt_list.append(1)
        if i == ')':
            if len(pt_list) == 0:
                return False
            del pt_list[0]

    return len(pt_list) == 0
