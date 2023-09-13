#!/usr/bin/python3

"""
A class of students
converted to json
"""


class Student:
    """Class Student defined below"""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
