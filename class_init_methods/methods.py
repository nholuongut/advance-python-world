from typing import Any


class B(type):
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        print("Meta class initialization")
        return super(B, cls).__call__(*args, **kwds)

    def __init__(cls, name, base, attr):
        print("First Initialize the meta class ontop of cls")
        print(cls, name, attr)


class A(metaclass=B):
    def __new__(cls, *args: Any, **kwds: Any):
        print("Heap allocation ")
        return super(A, cls).__new__(cls, *args, **kwds)

    def __init__(self, *args: Any, **kwds: Any) -> None:
        print("Object creation")
        super(A, self).__init__(*args, **kwds)


"""
metaclss design flow :

    step 1: initialize the meta class and then check rules ontop of super class which is A 
    step 2: then after go to meta class call method 
    step 3: initialize the class A 
            first go to __new__ method and allocate heap memeory
            then __init__ method initialize class A object
"""


class C(object):
    def __init__(self) -> None:
        print("Initialize class C")
        super(C, self).__init__()


if __name__ == "__main__":
    a = A()
    print(a)

    c = C()
    print(c)
