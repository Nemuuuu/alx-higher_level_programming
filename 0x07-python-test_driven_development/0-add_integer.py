#!/usr/bin/python3
def add_integer(a, b=98):
    """takes two arguments and returns their sum
    
    >>> add_integer(1,2)
    '1,2'
    
    """
    if type(a) is not int or type(b) is not int:
        if type(a) is float or type(b) is float:
            add = int(a) + int(b)
        elif type(a) is not int and type(a) is not float:
            raise TypeError("a must be an integer")
        elif type(b) is not int and type(b) is not float:
            raise TypeError("b must be an intger")
    else:
        add = a + b
    return add