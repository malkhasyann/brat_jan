""" Brat jan! This is the main module! """

import sys
import errors
from validity import *
from states import *
import io
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
            io.execute_bratwrite(line)
