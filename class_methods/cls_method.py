# Python program to demonstrate
# use of a class method and static method.
from datetime import date
from typing import Any, Dict


"""
Class Method vs Static Method

The basic difference between the class method vs Static method in Python and when to use the class method and static method in Python.

1. A class method takes cls as the first parameter while a static method needs no specific parameters.
2. A class method can access or modify the class state while a static method can’t access or modify it.
3. In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. 
On the other hand class methods must have class as a parameter.

4. We use @classmethod decorator in Python to create a class method and we use @staticmethod decorator to create a static method in Python.
"""


class Person:
    # define class variables
    details = "member"

    def __init__(self, name: str, age: int):
        """
        class object variables not access
        to class methods

        Args:
            name (_type_): name of the person
            age (_type_): age of the person
        """
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name: str, year: int):
        """
        define a cls method to output object
        with name , year

        Args:
            name (str): name of person
            year (int): name of year

        """
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age: int):
        """
        static methods utility methods no accessibility to clas variables

        Args:
            age (int): age of a person
        """
        return age > 18


person1 = Person("mayank", 21)
person2 = Person.fromBirthYear("mayank", 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
