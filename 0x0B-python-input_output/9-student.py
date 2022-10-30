#!/usr/bin/python3
""" defines Write a class Student that defines a student by
"""


class Student:
    """
    represent student
    """
    def __init__(self, first_name, last_name, age):
        """inicialization" new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary of student"""
        return self.__dict__