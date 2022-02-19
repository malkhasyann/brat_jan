""" Brat jan! This is the main module! """

import sys
import errors
import validity

filename = ""  # source file name
namespace = dict()  # namespace for variables
source_code = ""  # keeping whole code

keywords = ['if', 'elif', 'else', 'while', 'not', 'and', 'or',
            'bratjan', 'bratlsi']

comparisons = ['==', '!=', '<=', '>=', '<', '>']

if __name__ == "__main__":
    if validity.is_valid_source_argument():
        source_file = sys.argv[1]
    else:
        errors.file_not_found_error()

    with open(filename, 'r', encoding='utf-8') as file:
        source_code = file.readlines()
