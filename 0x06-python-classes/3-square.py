#!/usr/bin/python3
"""Square class to represent a square"""
class Square:
    """
    Defines a Square and its properties
    
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """
    def __init__(self,size=0):
        """initializes the size of the square.
        the size of the square can be specified otherwise
        default value will be assigned
        
        :param size: int size of square ( > 0)
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """calculate and return the area of the square"""
        Area = self.__size * self.__size
        return "{}".format(Area)