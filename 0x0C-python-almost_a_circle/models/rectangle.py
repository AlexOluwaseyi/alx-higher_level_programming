#!/usr/bin/python3

from models.base import Base
"""
Rectangle Models
Almost a circle project on ALX
"""


class Rectangle(Base):
    """
    Rectangle class

    Inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiates the Base models
        Instance attributes:
            width: width of rectangle
            height: height of rectangle
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns 'value' to width"""
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns 'value' to height"""
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Assigns 'value' to x"""
        if type(value) is not int:
            raise TypeError("x must be integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Assigns 'value' to y"""
        if type(value) is not int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints out the rectable using '#'"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update the values of variables
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """Override __str__ method to print custom string"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
                )
