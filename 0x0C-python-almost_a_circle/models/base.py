#!/usr/bin/python3
""" models/base.py """
import json
import csv


class Base:
    """
    Base class for managing id attribute in all future classes

    Private Class Attributes: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns:
          the list of the JSON string representation json_string.
          else: an empty list

        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set:

        Args:
            **dictionary (dict): "double pointer" to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return ([])

    def save_to_file_csv(cls, list_objs):
        """ Serializes list_obj in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes CSV file to a list of instances """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)] for key, value in d.items())
                              for d in list_dicts]
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return ([])
