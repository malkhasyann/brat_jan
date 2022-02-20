""" Brat jan! This is a module for execution code bodies. """

import expressions
import errors
import states
import write

namespace_stack = [states.namespace, ]  # stacking local namespaces


def define_body(index):
    """ Brat jan! Defines code body.
        Arguments:
              index -> current line index: int
        Returns body_code: str
    """
    body_code = []  # resulting code segment

    if states.source_code[index].strip() != '{':
        errors.syntax_error()

    i = 1  # line index counter
    try:
        while states.source_code[index + i].strip() != '}':
            body_code.append(states.source_code[index + i].strip())
            i += 1
        i += 1
    except IndexError:
        errors.syntax_error()

    return body_code, (index + i)


def body(lines: str):
    """ Brat jan! Executes lines of code segment.
        Arguments:
            lines -> code segment text: str
    """
    local_namespace = dict()  # creating new local namespace for this code block
    namespace_stack.append(local_namespace)  # appending current local namespace to the stack

    for line in lines:
        if line.startswith('bratwrite'):  # new variable is declared and assigned
            write.execute_bratwrite(line)
        elif line.startswith('bratjan'):  # printing
            expressions.execute_declaration_assignment(line, local_namespace)
        elif line.startswith('#'):  # comment line in brat jan language starts wit '#'
            continue
        if '=' == line.split()[1]:
            name = line.split()[0]
            for ns in range(len(namespace_stack), -1, -1):
                if name in ns:
                    expressions.execute_assignment(line, ns)
                    break
        else:  # no instruction category corresponds to this line
            errors.syntax_error()
    namespace_stack.pop()
