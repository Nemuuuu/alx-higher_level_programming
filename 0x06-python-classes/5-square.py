#!/usr/bin/python3
"""Square class to represent a square"""
class Square:
    """
    Defines a square and its basic properties
    
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """
    def __init__(self, size=0):
        """
        initializes the size of the square. the size can be specified
        unless it will assigns to default value 0
        
        :param size: int size of square ( > 0)
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be integer")
        if self.__size < 0:
            raise ValueError("size must be >+ 0")
        else:
            self.__size = size
    @property
    def size(self):
        """Retrieve the instance of attribute size"""
        return self.__size
    @size.setter
    def size(self, value):
        """
        Set the value of the size
        
        :param size: int size
        """
        if type(value) != 0:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """
        calculate and return the area of the square
        """
        return int(self.__size) ** 2
    def my_print(self):
        """
        print to stdout '#' * size
        """
        if self.__size != 0:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__size:
                    print("#",end="")
                    j+=1
                print()
                i+=1
        else:
            print()