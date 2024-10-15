"""singleton design pattern make sure only one object create from a class
"""

from typing import Any, Dict
from functools import wraps
import time
import logging


logging.basicConfig(
    filename="singleton_class/execution.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)


class MetaClass(type):
    """this is a singleton design pattern

    Args:
        type (_type_): type method
    """

    _instance: Dict[Any, Any] = {}
    _logger = logging.getLogger(__name__)

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        """function initialization make sure only one instance initiated

        Returns:
            Any: _description_
        """
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwds)
            return cls._instance[cls]
        else:
            print(
                "singleton protected class , not permited to create multiple instances"
            )

    def execution_time(func):  # type: ignore
        """measure function execution time

        Args:
            func (_type_): input function

        Returns:
            _type_: executed results
        """

        @wraps(func)
        def wrapper(self, *args: Any, **kwargs: Any):
            start_time = time.time()
            res = func(self, *args, **kwargs)
            end_time = time.time()
            print("function execution time :", end_time - start_time)
            return res

        return wrapper  # type: ignore

    def log(func):  # type: ignore
        """generate logs for function execution"""

        @wraps(func)
        def wrapper(self, *args: Any, **kwargs: Any):
            res = func(self, *args, **kwargs)
            print(kwargs)
            MetaClass._logger.info(
                f"function -> {kwargs.get('method_name')}   execution successed ."
            )
            return res

        return wrapper


class A(metaclass=MetaClass):
    def __init__(self) -> None:
        pass

    @MetaClass.execution_time  # type: ignore
    def timer(self, sleep_time: float):
        time.sleep(sleep_time)

    @MetaClass.log  # type: ignore
    def add(slef, a: int, b: int, method_name: str) -> int:
        return a + b


if __name__ == "__main__":
    obj = A()
    obj.timer(sleep_time=2)
    res = obj.add(a=20, b=40, method_name="add")
    print(obj, res)

    objb = A()
    print(objb)
