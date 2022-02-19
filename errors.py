""" Brat jan! This is a module for error messages! """

import sys


def file_extension():
    print('Brat jan! Brat jan files have ".bj" extension! ')
    sys.exit()


def file_not_found_error():
    print("Brat jan! File not found error.")
    sys.exit()


def syntax_error():
    print(f"Brat jan! Syntax error.")
    sys.exit()


def zero_division_error():
    print(f"Brat jan! Zero division error.")
    sys.exit()


def already_declared_name_error(n):
    print(f"Brat jan! \"{n}\" name is busy!")
    sys.exit()
