# Method 1:

"""
Lazy Properties

The first and most straightforward example is lazy properties. These are properties whose initial values are not loaded until they’re accessed for the first time. 
Then, they load their initial value and keep that value cached for later reuse.


"""

# slow_properties.py
import time


class DeepThought:
    def meaning_of_life(self):
        time.sleep(3)
        return 42


my_deep_thought_instance = DeepThought()
print("\n With out descriptor \n")
print(my_deep_thought_instance.meaning_of_life())
print(my_deep_thought_instance.meaning_of_life())
print(my_deep_thought_instance.meaning_of_life())


"""
Now, a lazy property can instead evaluate this method just once when it’s first executed. Then, it will cache the resulting value so that, if you need it again, 
you can get it in no time. You can achieve this with the use of Python descriptors:
"""
# lazy_properties.py
import time
from typing import Any


class LazyProperty:
    """
    non data descriptor (without __set__ )
    """

    def __init__(self, function: Any):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj: Any, type: Any = None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]


class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42


my_deep_thought_instance = DeepThought()
print("\n With Lazy Evaluation \n")
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)

"""
Since it is a non-data descriptor, when you first access the value of the meaning_of_life attribute, .__get__() is automatically called and executes 
.meaning_of_life() on the my_deep_thought_instance object. The resulting value is stored in the __dict__ attribute of the object itself. 
When you access the meaning_of_life attribute again, 
Python will use the lookup chain to find a value for that attribute inside the __dict__ attribute, and that value will be returned immediately.
"""


"""
. If you had implemented a data descriptor, then the trick would not have worked. Following the lookup chain, 
it would have had precedence over the value stored in __dict__.
 To test this out, run the following code:
"""

# wrong_lazy_properties.py
import time


class LazyProperty:
    def __init__(self, function: Any):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj: Any, type: Any = None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

    def __set__(self, obj: Any, value: Any):
        pass


class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42


my_deep_thought_instance = DeepThought()
print("With Lazy Evaluation but with data descriptor")
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)


# Methods 2:

"""
D.R.Y. Code

Another typical use case for descriptors is to write reusable code and make your code D.R.Y. 
Python descriptors give developers a great tool to write reusable code that can be shared among different properties or even different classes.
"""


# wrong approach


# properties.py
class Values:
    def __init__(self):
        # define private variables
        self._value1 = 0
        self._value2 = 0
        self._value3 = 0
        self._value4 = 0
        self._value5 = 0

    # drawback of the below workaround is that for every private variable need to have seperate get,settr method

    @property
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value if value % 2 == 0 else 0

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, value):
        self._value2 = value if value % 2 == 0 else 0

    @property
    def value3(self):
        return self._value3

    @value3.setter
    def value3(self, value):
        self._value3 = value if value % 2 == 0 else 0

    @property
    def value4(self):
        return self._value4

    @value4.setter
    def value4(self, value):
        self._value4 = value if value % 2 == 0 else 0

    @property
    def value5(self):
        return self._value5

    @value5.setter
    def value5(self, value):
        self._value5 = value if value % 2 == 0 else 0


my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print("\n Python multiple private object handle \n")
print(my_values.value1)
print(my_values.value2)


"""
As you can see, you have a lot of duplicated code here. It’s possible to use Python descriptors to share behavior among all the properties. 
You can create an EvenNumber descriptor and use it for all the properties like this:
"""


class Descriptor:
    def __set_name__(self, owner: Any, name: Any) -> None:
        self.name = name

    def __get__(self, obj: Any, type: Any):
        print("__get__", obj)
        return obj.__dict__[self.name] if obj.__dict__.get(self.name) else 0

    def __set__(self, obj: Any, value: Any):
        print("__set__", obj)
        obj.__dict__[self.name] = value if value % 2 == 0 else 0

    def __delete__(self, obj: Any):
        del obj.__dict__[self.name]


class Values:
    value1 = Descriptor()
    value2 = Descriptor()
    value3 = Descriptor()


# initialize the class object

obj = Values()
obj.value1 = 2
obj.value2 = 1
print("\n Define descriptor ")
print(obj.value1, obj.value2)

obj1 = Values()
print(obj1.value1)
