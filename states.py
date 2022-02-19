""" Brat jan! This module keeps dynamic data"""

filename = ""  # source file name
namespace = dict()  # namespace for variables
source_code = ""  # keeping whole code
instruction_segment = []  # caching intsructions for conditionals or loops

keywords = ['if', 'elif', 'else', 'while', 'not', 'and', 'or',
            'bratjan', 'bratwrite']
