""" Brat jan! This is a module for execution code bodies. """

import expressions
import errors
import states
import write

namespace_stack = [states.namespace, ]  # stacking local namespaces


def define_body():
    pass


def body(lines: str):
    """ Brat jan! Executes lines of code segment.
        Arguments:
            lines -> code segment text: str
    """
    local_namespace = dict()  # creating new local namespace for this code block
    namespace_stack.append(local_namespace) # appending current local namespace to the stack

    for line in lines:
        if line.startswith('bratwrite'):  # new variable is declared and assigned
            write.execute_bratwrite(line)
        elif line.startswith('bratjan'):  # printing
            expressions.execute_declaration_assignment(line, local_namespace)
        elif line.startswith('#'):  # comment line in brat jan language starts wit '#'
            continue
        if '=' in line:
            name = line.split()[0]
            for ns in range(len(namespace_stack), -1, -1):
                if name in ns:
                    expressions.execute_assignment(line, ns)
                    break
        else:  # no instruction category corresponds to this line
            errors.syntax_error()
    namespace_stack.pop()