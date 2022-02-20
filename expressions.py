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

    # for printing string literal

    string_elements = []
    is_string = False
    start_index = -1
    end_index = -1
    i = 0
    while i < len(splitted_expr):
        if splitted_expr[i].startswith('"'):
            start_index = i
            is_string = True
        if is_string:
            string_elements.append(splitted_expr[i])
        if splitted_expr[i].endswith('"'):
            end_index = i
            break
        i += 1
    string = " ".join(string_elements)
    del splitted_expr[start_index: end_index + 1]
    if len(string) > 0:
        splitted_expr.insert(start_index, string)

    for i, elem in enumerate(splitted_expr):
        if validity.is_valid_var_name(elem):
            if elem in ns:
                splitted_expr[i] = str(ns[elem])
            else:
                errors.name_not_defined_error(elem)

    expr = " ".join(splitted_expr)
    return expr


def execute_expression(expr: str, ns=None):
    """ Brat jan! Executes the expression. """
    if ns is None:
        ns = states.namespace

    # if the value is string, not to lose its quotes
    if expr.startswith('"') and expr.endswith('"'):
        return expr

    try:
        expr = replace_var_name_by_value(expr)
        result = str(eval(expr))
    except (SyntaxError, NameError, ValueError, ZeroDivisionError):
        errors.syntax_error()
        result = None

    return result


def execute_declaration_assignment(instruction: str, ns=None):
    """ Brat jan! Executes Declaration-Assignment"""
    if ns is None:
        ns = states.namespace

    splitted_instr = instruction.split('=')
    if len(splitted_instr) != 2:
        errors.syntax_error()

    value_expr = splitted_instr[1].strip()  # value expression to be assigned in str
    dec, name = splitted_instr[0].split()  # declaration, var name

    if dec != 'bratjan' or not validity.is_valid_var_name(name):
        errors.syntax_error()

    if name in ns:
        errors.already_declared_name_error(name)

    value = execute_expression(value_expr)
    ns[name] = value


def execute_assignment(instruction: str, ns=None):
    """ Brat jan! Executes Assignment. """
    if ns is None:
        ns = states.namespace

    splitted_instr = instruction.split('=')
    if len(splitted_instr) != 2:
        errors.syntax_error()

    value_expr = splitted_instr[1].strip()  # value expression to be assigned in str
    name = splitted_instr[0].strip()  # var name

    if not validity.is_valid_var_name(name):
        errors.syntax_error()

    if name not in ns:
        errors.name_not_defined_error(name)

    value = execute_expression(value_expr)
    ns[name] = value
