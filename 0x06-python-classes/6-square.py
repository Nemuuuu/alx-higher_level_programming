#!/usr/bin/python3
"""Square class to represent a square"""

class Square:
    """
    Defines a square and its properties
    
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes the size of the square. 
        the size can be specified unless it will be value of 0
        
        :param size: int size of square ( > 0)
        :param: tuple (x, y) representing position
        """
        self.__size = size
        self.__position = position
        if type(self.__size) != int:
            raise TypeError("size must be integer")
        if self.__size < 0:
            raise ValueError("size must be >+ 0")
        else:
            self.__size = size
    @property
    def size(self):
        """
        Retreive instance attribute size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Set the value of the size
        
        :param: int size
        """
        if type(value) != 0:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """
        calculate and return area of square
        """
        return int(self.__size) ** 2
    def my_print(self):
        """
        prints '#' to stdout
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
    @property
    def position(self):
        """
        Retrieves the instance of attribute position
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
        Set the position
        
        :param: (x, y)
        """
        if len(value) != 2:
            if value < 0 or type(value) != int:
                raise TypeError("position must be a tuple of 2 positive integers")