#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect = ""
            for i in range (self.__height):
                for j in range (self.__width):
                    rect += str(self.print_symbol)
                if i < self.__height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")