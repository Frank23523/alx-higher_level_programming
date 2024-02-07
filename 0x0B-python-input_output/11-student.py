#!/usr/bin/python3
"""A class Student"""


class Student:
    """This is a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json (dict): A dictionary containing attribute-value pairs
        """
        for attr, value in json.items():
            setattr(self, attr, value)
