""" Brat jan! This is a module for error messages! """

import sys


def source_file_error():
    print("Brat jan! Invalid source file error.")
    sys.exit()


def syntax_error():
    print(f"Brat jan! Syntax error.")
    sys.exit()


def zero_division_error():
    print(f"Brat jan! Zero division error.")
    sys.exit()


def name_not_defined_error(n):
    print(f"Brat jan! \"{n}\" name is not defined!")
    sys.exit()


def already_declared_name_error(n):
    print(f"Brat jan! \"{n}\" name is busy!")
    sys.exit()


def total_crash():
    print("Brat jan! Zgush exi, nurb gorciq a...")
    sys.exit()
