""" Brat jan! This module helps solve complex expressions. """

import errors
import states
import validity


def replace_var_name_by_value(expr: str, ns: dict):
    """ Brat Jan! Replace variable names in expressions by their values
        Arguments:
            expr -> the expression
            ns -> namespace of variables
    """
    splitted_expr = expr.split()
    for i, elem in enumerate(splitted_expr):
        if elem in ns:
            splitted_expr[i] = str(ns[elem])

    expr = " ".join(splitted_expr)
    return expr


def execute_expression(expr: str, ns: dict):
    """ Brat jan! Executes the expression.
        Arguments:
            expr -> the expression
            ns -> namespace of variables
    """
    try:
        expr = replace_var_name_by_value(expr, states.namespace)
        result = str(eval(expr))
    except (SyntaxError, NameError, ValueError, ZeroDivisionError):
        errors.syntax_error()

    return result


def execute_assignment(instruction: str):
    """ Brat jan! Executes Assignment"""

    splitted_instr = instruction.split('=')
    if len(splitted_instr) != 2:
        errors.syntax_error()

    value_expr = splitted_instr[1].strip()  # value expression to be assigned in str
    dec, name = splitted_instr[0].split()  # declaration, var name

    if dec != 'bratjan' or not validity.is_valid_var_name(name):
        errors.syntax_error()

    if name in states.namespace:
        errors.already_declared_name_error()

    value = execute_expression(value_expr)
    states.namespace[name] = value

# def check_parentheses(s: str):
#     """ Brat jan! Checks whether parentheses are putted properly.
#         Arguments:
#             s -> text to check : str
#     """
#     pt_list = []  # parentheses history list
#     for i in s:
#         if i == '(':
#             pt_list.append(1)
#         if i == ')':
#             if len(pt_list) == 0:
#                 return False
#             del pt_list[0]
#
#     return len(pt_list) == 0
#
#
# def broke_expr_by_parentheses(expr):
#     if not check_parentheses(expr):
#         errors.syntax_error()
#     pass
