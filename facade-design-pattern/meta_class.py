from typing import Any, Dict, List
from functools import wraps
import time
import sys
import logging
from logger import Logger


# define a metaclass & logging method
class MetaClass(type):
    """
    singleton design pattern
    """

    _instances: Any = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        first __call__ method assign memory to heap
        """
        if cls not in cls._instances:
            """define the class instance & return class instance
            super method instanciate the Metaclass with cls & check the cls imposed rules
            thens econd __call__ create the class object
            """
            cls._instances[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instances[cls]

    def __init__(cls, name, base, attr):
        """
        impose class rules
        """
        print("Checking Class Impose Rules : ", name)

        # rule 1: class name start with capital letter
        if cls.__name__[0].isupper():
            # check every attribute and check for first letter simple
            for k, v in attr.items():  # type: ignore
                if hasattr(v, "__call__"):  # type: ignore
                    if v.__name__[0] == "_" or v.__name__[0].islower():  # type: ignore
                        # check for methods doc strings
                        if v.__doc__ is None:  # type: ignore
                            raise ValueError("Make sure provide Doc strings ...")

                        else:
                            pass
                    else:
                        # raise error when method start name is not lowercase
                        raise ValueError(
                            "class method should start with lower case : {}".format(
                                v.__name__
                            )
                        )
        else:
            # raise error when class name is not start with upper case
            raise ValueError(
                "class name should be start with upper case letter : {}".format(
                    cls.__name__
                )
            )
