""" Brat jan! This module helps solve complex expressions. """

import errors
import states
import validity


def replace_var_name_by_value(expr: str, ns=None):
    """ Brat Jan! Replace variable names in expressions by their values
        Arguments:
            expr -> the expression
            ns -> namespace of variables
    """
    if ns is None:
        ns = states.namespace

    splitted_expr = expr.split()
    for i, elem in enumerate(splitted_expr):
        if elem.isalnum():
            if elem in ns:
                splitted_expr[i] = str(ns[elem])
            else:
                errors.name_not_defined_error(elem)

    expr = " ".join(splitted_expr)
    return expr


def execute_expression(expr: str):
    """ Brat jan! Executes the expression.
        Arguments:
            expr -> the expression
            ns -> namespace of variables
    """
    try:
        expr = replace_var_name_by_value(expr)
        result = str(eval(expr))
    except (SyntaxError, NameError, ValueError, ZeroDivisionError):
        errors.syntax_error()
        result = None

    return result


def execute_declaration_assignment(instruction: str):
    """ Brat jan! Executes Declaration-Assignment"""

    splitted_instr = instruction.split('=')
    if len(splitted_instr) != 2:
        errors.syntax_error()

    value_expr = splitted_instr[1].strip()  # value expression to be assigned in str
    dec, name = splitted_instr[0].split()  # declaration, var name

    if dec != 'bratjan' or not validity.is_valid_var_name(name):
        errors.syntax_error()

    if name in states.namespace:
        errors.already_declared_name_error(name)

    value = execute_expression(value_expr)
    states.namespace[name] = value


def execute_assignment(instruction: str):
    """ Brat jan! Executes Assignment"""

    splitted_instr = instruction.split('=')
    if len(splitted_instr) != 2:
        errors.syntax_error()

    value_expr = splitted_instr[1].strip()  # value expression to be assigned in str
    name = splitted_instr[0].strip()  # var name

    if not validity.is_valid_var_name(name):
        errors.syntax_error()

    if name not in states.namespace:
        errors.name_not_defined_error(name)

    value = execute_expression(value_expr)
    states.namespace[name] = value
