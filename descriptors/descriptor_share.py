# descriptors2.py
class OneDigitNumericValue:
    def __init__(self):
        self.value = 0

    def __get__(self, obj, type=None) -> object:
        return self.value

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value


class Foo:
    number = OneDigitNumericValue()


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

"""
warning ! 

Here, you have a class Foo that defines an attribute number, which is a descriptor. This descriptor accepts a single-digit numeric value and stores it in a property of the descriptor itself. 
However, this approach won’t work, because each instance of Foo shares the same descriptor instance.
What you’ve essentially created is just a new class-level attribute.

"""
