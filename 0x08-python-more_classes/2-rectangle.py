#!/usr/bin/python3
"""Rectangle class to represent rectangle property
"""

class Rectangle:
	"""Define Rectangle with properties of rectangle
	"""

    def __init__(self, width=0, height=0):
	"""Initializes width and height of rectangle
	""""

        self.__width = width
        self.__height = height
    @property
    def width(self):
	"""to retrieve width
	
	Returns:
		width of rectangle
	"""
        return self.__width
    @width.setter
    def width(self, value):
	"""to set value to width
	
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
	"""to retrieve height

	Returns:
		height of rectangle
	"""
        return self.__height
    @height.setter
    def height(self, value):
	"""to set value to height

	Raises:
		TypeError: if height is not integer
		ValueError: if height < 0
	"""
        self.__height = value
        if (type(self.__height) != int):
            raise TypeError("width must be an integer")
        if (self.__height <= 0):
            raise ValueError("width must be >= 0")
    def area(self):
	"""calculates area of rectangle

	Returns:
		area of rectangle
	"""
        return self.__height * self.__width
    def perimeter(self):
	"""calculates perimeter of rectangle

	Returns:
		perimeter of rectangle
	"""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * self.__width + 2 * self.__height
        return perimeter
