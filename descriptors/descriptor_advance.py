from typing import Any

# define descriptor function
"""
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None

In .__set__(), you don’t have the type variable, because you can only call .__set__() on the object. 
In contrast, you can call .__get__() on both the object and the class.


warning !

Another important thing to know is that Python descriptors are instantiated just once per class. 
That means that every single instance of a class containing a descriptor shares that descriptor instance. 
This is something that you might not expect and can lead to a classic pitfall, like this:

The best solution here is to simply not store values in the descriptor itself, 
but to store them in the object that the descriptor is attached to
"""


class Descriptor:
    def __set_name__(self, owner: Any, name: Any):
        self.name = name

    def __get__(self, obj: Any, type: Any) -> Any:
        print("__get__")
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj: Any, value: Any) -> None:
        print("__set__")
        obj.__dict__[self.name] = value

    def __delete__(self, obj: Any) -> None:
        print("__delete__")
        del obj.__dict__[self.name]


class Memeber:
    number = Descriptor()


if __name__ == "__main__":
    obj = Memeber()
    obj.number = 10

    obj2 = Memeber()
    obj2.number = 20

    print(obj.number)
    print(obj2.number)

    """
    Why Use Python Descriptors?

    The first and most straightforward example is lazy properties. These are properties whose initial values are not loaded until they’re accessed for the first time. 
    Then, they load their initial value and keep that value cached for later reuse.

    """
