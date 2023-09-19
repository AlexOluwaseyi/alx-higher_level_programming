#!/usr/bin/python3

from models.rectangle import Rectangle
"""
Rectangle Models
Almost a circle project on ALX
"""


class Square(Rectangle):
    """
    The Square model based on the Rectangle model
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square initialization
        Instance attributes:
            size: size of the sides of the square
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square's attributes."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """String representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )
