""" Brat jan! This is the main module! """

import sys
import errors
from validity import *

filename = ""  # source file name
namespace = dict()  # namespace for variables
source_code = ""  # keeping whole code

keywords = ['if', 'elif', 'else', 'while', 'not', 'and', 'or',
            'bratjan', 'bratlsi']

comparisons = ['==', '!=', '<=', '>=', '<', '>']

if __name__ == "__main__":
    if is_valid_source_argument():
        filename = sys.argv[1]
    else:
        errors.source_file_error()

    with open(filename, 'r', encoding='utf-8') as file:
        source_code = file.readlines()

    for line in source_code:
        print(line)
