from typing import Any


class CountCalls():
    def __init__(self, func_init=None) -> None:
        self.func_init = func_init
        self.num_calls = 0
        self.route_call =0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.num_calls +=1
        print("This is executed :", self.num_calls)
        return self.func_init(*args, **kwargs)
    
    def route_func(self , rule , **options):
        def wrapper(func):
            self.route_call +=1
            print("Route call : ", self.route_call)
            return func
        return wrapper


@CountCalls
def hello():
    print("Hello world")

hello()
hello()



count_call = CountCalls()

@count_call.route_func("/")
def greeting():
    print("Hello Greetings !!")

greeting()



################## decorators inside class #####################

import functools


class Example:

    def wrapper(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            print("inside wrap")
            return func(self, *args, **kwargs)
        return wrap

    @wrapper
    def method(self):
        print("METHOD")

    wrapper = staticmethod(wrapper)


e = Example()
e.method()