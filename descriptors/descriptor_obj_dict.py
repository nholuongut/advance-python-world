# descriptors3.py
class OneDigitNumericValue:
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value


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
Unfortunately, the downside here is that the descriptor is keeping a strong reference to the owner object. This means that if you destroy the object, 
then the memory is not released because the garbage collector keeps finding a reference to that object inside the descriptor!

"""
