""" Brat jan! This module helps solve complex expressions. """

import errors
import states

#
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


def replace_var_name_by_value(expr: str, ns: dict):
    """ Brat Jan! Replace variable names in expressions by their values
        Arguments:
            expr -> the expression
            ns -> namespace of variables
    """
    for elem in expr.split():
        if elem in ns:
            expr = expr.replace(elem, str(ns[elem]))

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
