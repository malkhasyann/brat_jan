""" Brat jan! This is the main module! """

import errors
import loops
import states
from validity import *
import write
import expressions
import conditionals

if __name__ == "__main__":
    if is_valid_source_argument():
        filename = sys.argv[1]
    else:
        errors.source_file_error()
        filename = None

    with open(filename, 'r', encoding='utf-8') as file:
        states.source_code = file.readlines()
        states.source_code.append('')

    index = 0
    while index < len(states.source_code):
        line = states.source_code[index]  # holding current code line by its index

        if line.startswith('bratwrite'):  # new variable is declared and assigned
            write.execute_bratwrite(line)
        elif line.startswith('bratjan'):  # printing
            expressions.execute_declaration_assignment(line)
        elif line.startswith('#'):  # comment line in brat jan language starts wit '#'
            pass
        elif line.strip() == '':  # empty line
            pass
        elif line.split()[0] in states.namespace and '=' in line:
            expressions.execute_assignment(line)
        elif line.split()[0] == 'if':
            index = conditionals.if_execution(index, line)
            continue
        elif line.split()[0] == 'while':
            index, state = loops.while_execution(index, line)
        else:  # no instruction category corresponds to this line
            errors.syntax_error()

        index += 1  # go to newline index
