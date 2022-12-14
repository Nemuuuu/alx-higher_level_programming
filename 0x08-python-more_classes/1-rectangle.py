#!/usr/bin/python3
"""Rectangle to represent a rectangle
"""

class Rectangle:
    """Defines a Rectangle and its basic properties
    """
    
    def __init__(self, width=0, height=0):
        """Called when object is created.
        Args:
            width (int): defines width of rectangle
            height (int): defines height of rectangle
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """retrieve width.
        
        Returns:
            width of rectangle
        """
        return self.__width
    @width.setter
    def width(self, value):
        """set the value of width
        Args:
            value (int): sets the the value of width variable
        Raises:
            TypeError: if width is not integer
            ValueError: if width < 0
        """
        self.__width = value
        if (type(self.__width) != int):
            raise TypeError("width must be an integer")
        if (self.__width <= 0):
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        """retrieves height
        
        Returns:
            height of rectangle
        """
        return self.__height
    @height.setter
    def height(self, value):
        """set the value of height
        Args:
            value (int): sets the value of height variable
        Raises:
            TypeError: if height is not integer
            ValueError: if height < 0
        """
        self.__height = value
        if (type(self.__height) != int):
            raise TypeError("height must be an integer")
        if (self.__height <= 0):
            raise ValueError("height must be >= 0")
