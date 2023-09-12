#!/usr/bin/python3


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class is for defining geometric shapes and performing
    calculations related to them.

    Methods:
        area(): Raises an Exception with message 'area() is not implemented'.
            This method is meant to be overridden by derived classes to
            provide specific implementation for calculating area.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        This method is meant to be overridden by derived classes to
        provide specific implementation for calculating area.
        """
        raise Exception('area() is not implemented')
