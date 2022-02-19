""" Brat jan! This module keeps dynamic data"""

filename = ""  # source file name
namespace = dict()  # namespace for variables
source_code = ""  # keeping whole code
body_stack = []  # keeping intsructions for conditionals or loops

keywords = ['if', 'elif', 'else', 'while', 'not', 'and', 'or',
            'bratjan', 'bratwrite']
