#!/usr/bin/python3
"""8-rectangle, built for Holberton Python project 0x08 task 1.
"""


class Rectangle:
    """Takes in args for width and height of a rectangle, and contains methods
    for calculation of the area or perimeter.

    __str__
    __repr__
    __del__

    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__width getter.

        Returns:
        __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
        value (int): vertical dimension of rectangle

        Attributes:
        __height (int): vertical dimension of rectangle

        Raises:
        TypeError: If `value` is not an int.
        ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            A string representing the rectangle using '#' characters.

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __repr__(self):
        """Returns a string representation that can recreate the instance.

        Returns:
        A string representation that can recreate the instance using eval().

        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when an instance is deleted.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
