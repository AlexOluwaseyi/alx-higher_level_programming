#!/usr/bin/python3
"""
Base class
Almost a circle project on ALX
"""

import json
import csv
import turtle


class Base:
    """
    Base class for project
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initiates the Base models
        Args:
            Takes None or one argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list from a JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            dictionary (dict): A dictionary containing attribute values.

        Returns:
            Base: An instance with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_data = file.read()
                data_list = cls.from_json_string(json_data)
                for data in data_list:
                    instance = cls.create(**data)
                    instance_list.append(instance)

        except FileNotFoundError:
            return []

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to a CSV file.

        Args:
            list_objs (list): A list of instances to be serialized.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y]
                            )

            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.

        Returns:
            list: A list of instances deserialized from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        instance = cls(
                                int(row[1]), int(row[2]),
                                int(row[3]), int(row[4]), int(row[0])
                                )
                        instance_list.append(instance)

                    elif cls.__name__ == "Square" and len(row) == 4:
                        instance = cls(
                                int(row[1]), int(row[2]),
                                int(row[3]), int(row[0])
                                )
                        instance_list.append(instance)

        except FileNotFoundError:
            return []

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares using the turtle graphics module.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        t = turtle.Turtle()
        t.speed(0)
        t.bgcolor("white")

        # Draw rectangles
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        # Draw squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        t.exitonclick()
