#!/usr/bin/python3
"""Integer validator for geometry"""


class BaseGeometry:
    """
    A class definition for a geometry
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        This method is meant to be overridden by derived classes to
        provide specific implementation for calculating area.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
