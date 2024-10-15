"""
decorator :
function decorator : fucntions inpython are first class citizens
class decorator
"""
import functools

def start_end_decorator(func):

    # below decorator helps to keep the identity of the func otherwise takes as wrapper
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        print("start")
        res = func(*args , **kwargs)
        print("end")
        return res
    
    return wrapper

# @start_end_decorator
# def print_name():
#     print("alex")

##### add arguments to decorators
@start_end_decorator
def add(x):
    return x+5

#print_name = start_end_decorator(print_name)

res = add(10)
print(res)
#print(help(add))
print(add.__name__)



########## decorator arguments

def repeat(num_items):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args , **kwargs):
            for _ in range(num_items):
                result = func(*args , **kwargs)
            return result
        return wrapper
    return decorator_repeat



@repeat(num_items=4)
def greet(name):
    print("Hello {}".format(name))

greet("Himasha")


############ nested decorators

def first_decorator(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        print("Start")
        result = func(*args , **kwargs)
        print("End")
        return result
    
    return wrapper


def second_decorator(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        args_repr = [ repr(a) for a in args ]
        kwargs_repr = [ f"{key}-{val}" for key , val in kwargs.items() ]
        signature = ", ".join(args_repr+kwargs_repr)
        print(f"Calling {func.__name__} ( {signature} )")
        result = func(*args , **kwargs)
        print(f"{func.__name__} retunred {result}")
        return result
    return wrapper


@second_decorator
@first_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello("Alex")
