#!/usr/bin/pytho3
"""Square class to represent a square"""
class Square:
    """
    Defines a Square and its basic properties
        
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """
    size = 0
    def __init__(self, size=0):
        """
        initializes the size of the square. the size can be specified unless assigned to default 
        
        :param size: int size of square ( > 0)
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    @property
    def size(self):
        """Retrieve the instance attribute size"""
        return self.__size
    @size.setter
    def size(self, value):
        """
        Set the value of size
        
        :param: int size
        """
        if type(value) != 0:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """calculates and returns the area of square"""
        return int(self.__size) ** 2