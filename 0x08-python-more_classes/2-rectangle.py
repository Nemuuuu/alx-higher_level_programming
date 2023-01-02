#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
        if (type(self.__width) != int):
            raise TypeError("width must be an integer")
        if (self.__width <= 0):
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
        if (type(self.__height) != int):
            raise TypeError("width must be an integer")
        if (self.__height <= 0):
            raise ValueError("width must be >= 0")
    def area(self):
        return self.__height * self.__width
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * self.__width + 2 * self.__height
        return perimeter