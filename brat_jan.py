""" Brat jan! This is the main module! """

import errors
from validity import *
import write
import expressions

if __name__ == "__main__":
    if is_valid_source_argument():
        filename = sys.argv[1]
    else:
        errors.source_file_error()
        filename = None

    with open(filename, 'r', encoding='utf-8') as file:
        source_code = file.readlines()

    for line in source_code:
        if line.startswith('bratwrite'):
            write.execute_bratwrite(line)
        if line.startswith('bratjan'):
            expressions.execute_declaration_assignment(line)

