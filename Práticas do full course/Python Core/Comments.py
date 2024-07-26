# This is a comment

"""
   A 
   multi-line 
   comment
"""


# Docstrings is a comment that is not omitted by interpreter. It's used in describing classes.

a = 4


def square(a):
    """ Returned argument a is squared. """
    return a ** a


print(square.__doc__)
