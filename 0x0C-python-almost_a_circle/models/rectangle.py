#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def convert_to_json_string(list_of_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_of_dictionaries (list): A list of dictionaries.
        """
        if list_of_dictionaries is None or list_of_dictionaries == []:
            return "[]"
        return json.dumps(list_of_dictionaries)

    @classmethod
    def save_to_file(cls, list_of_objects):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_of_objects (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_of_objects is None:
                json_file.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_of_objects]
                json_file.write(Base.convert_to_json_string(list_of_dicts))

    @staticmethod
    def convert_from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_of_dicts = Base.convert_from_json_string(json_file.read())
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objects):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_of_objects (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_of_objects is None or list_of_objects == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                for obj in list_of_objects:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_of_dicts = csv.DictReader(csv_file, fieldnames=field_names)
                list_of_dicts = [dict([k, int(v)] for k, v in d.items())
                                  for d in list_of_dicts]
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_of_rectangles, list_of_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_of_rectangles (list): A list of Rectangle objects to draw.
            list_of_squares (list): A list of Square objects to draw.
        """
        turtle_obj = turtle.Turtle()
        turtle_obj.screen.bgcolor("#b7312c")
        turtle_obj.pensize(3)
        turtle_obj.shape("turtle")

        turtle_obj.color("#ffffff")
        for rect in list_of_rectangles:
            turtle_obj.showturtle()
            turtle_obj.up()
            turtle_obj.goto(rect.x, rect.y)
            turtle_obj.down()
            for i in range(2):
                turtle_obj.forward(rect.width)
                turtle_obj.left(90)
                turtle_obj.forward(rect.height)
                turtle_obj.left(90)
            turtle_obj.hideturtle()

        turtle_obj.color("#b5e3d8")
        for sq in list_of_squares:
            turtle_obj.showturtle()
            turtle_obj.up()
            turtle_obj.goto(sq.x, sq.y)
            turtle_obj.down()
            for i in range(2):
                turtle_obj.forward(sq.width)
                turtle_obj.left(

