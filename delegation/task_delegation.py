"""
Delegation is another technique that you can use as an alternative to inheritance. With delegation, you can model can-do relationships, 
where an object hands a task over to another object, which takes care of executing the task. 
Note that the delegated object can exist independently from the delegator.



Finally, in Python, you can quickly implement delegation through the .__getattr__() special method. 
Python calls this method automatically whenever you access an instance attribute or method. 
You can use this method to redirect the request to another object that can provide the appropriate method or attribute.
"""

import json
import pickle
from typing import Any


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


class Serializer:
    def __init__(self, instance: object) -> None:
        self.instance = instance

    def to_json(self):
        return json.dumps(self.instance.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.instance.__dict__)


class Employee(Person):
    def __init__(self, name: str, age: int, salary: float) -> None:
        super().__init__(name, age)
        self.salary = salary

    def __getattr__(self, attr):
        return getattr(Serializer(self), attr)


if __name__ == "__main__":
    employee = Employee(name="Himasha", age=28, salary=1680.00)

    # call the delegation method
    print(Employee.__mro__)
    print(employee.name)
    ## to_json() on an instance of Employee, then that call will be automatically redirected to calling .to_json() on the instance of Serializer
    print(employee.to_json())
    print(employee.to_pickle())
    print(employee.get_name())
