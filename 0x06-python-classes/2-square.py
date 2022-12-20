#!/usr/bin/python3
"""Square class to  represent a square"""
class Square:
    """
    Defines a Square and its properties
    
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """
    def __init__(self,size=0):
        """
        initialize the size of the square.
        if the size is not specified the defailt will be 0
        
        :param size: int size of square ( > 0)
        """
        self.__size = size
        if type(self.__size) != int:
            message = "size must be an integer"
            raise TypeError(message)
        if self.__size < 0:
            raise ValueError("size must be >= 0")