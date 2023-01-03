#!/usr/bin/python3
"""Rectangle to represent a rectangle
"""

class Rectangle:
    """Defines a Rectangle and its basic properties
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Called when object is created.
        Args:
            width (int): defines width of rectangle
            height (int): defines height of rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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
    def area(self):
        """calculates and returns area of rectangle
        """
        return self.__height * self.__width
    def perimeter(self):
        """calculates and return perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * self.__width + 2 * self.__height
        return perimeter
    def __str__(self):
        """Unfficial representation of rectangle
        """
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect
    def __repr__(self):
        """Official representation of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """Deleting
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method, compares two rectangle and returns the bigger one
        """
        if type(rect_1) is Rectangle and type(rect_2)  is Rectangle:
            if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
                return rect_1
            else:
                return rect_2
        else:
            if type(rect_1) != Rectangle:
                raise TypeError("rect_1 must be an instance of Rectangle")
            if type(rect_2) != Rectangle:
                raise TypeError("rect_2 must be an instance of Rectangle")
    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance
        """
        return cls(size, size)
