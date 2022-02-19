""" Brat jan! This module is for validity checkers. """

import sys
import states


def is_valid_source_argument():
    """ Brat jan! Checks whether source code argument is passed properly. """

    if len(sys.argv) == 2 and sys.argv[1].split('.')[-1] == 'bj':
        return True
    return False


def is_valid_var_name(name: str):
    """ Brat jan! Checks whether var name is given properly. """
    if (ord(name[0]) not in range(65, 91)
            and ord(name[0]) not in range(97, 123)):
        return False

    if name in states.keywords:
        return False
    return True
