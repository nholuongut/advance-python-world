from typing import Dict, List, Any
import logging
import time
import sys
from functools import wraps


class Logger:
    _logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        self.set_handlers()

    @classmethod
    def set_handlers(cls) -> None:
        info_handler = logging.FileHandler(filename="logs/info_logs.log")
        error_handler = logging.FileHandler(filename="logs/error_logs.log")

        # set logging levels
        info_handler.setLevel(level=logging.DEBUG)
        error_handler.setLevel(level=logging.ERROR)

        # set format
        format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        info_handler.setFormatter(format)
        error_handler.setFormatter(format)

        cls._logger.addHandler(info_handler)
        cls._logger.addHandler(error_handler)

    @classmethod
    def log(cls, func: Any) -> Any:
        # wrap the function
        @wraps(func)
        def wrapper(self, *args: Any, **kwargs: Any) -> Any:
            # track time
            start_time = time.time()

            # execute funtion
            result = func(self, *args, **kwargs)

            # track end time
            end_time = time.time()

            # total memory usage
            memoryUsage = sys.getsizeof(func)
            func_name = func.__name__
            message = f"Function : {func_name}\n\
                        MemoryUsage : {memoryUsage} Bytes\n\
                        Time : {end_time-start_time}\n\
                    "
            # logg message
            cls._logger.debug(message)

            return result

        return wrapper

    def log_info(self, message: str) -> None:
        self._logger.debug(message)

    def log_error(self, message: str) -> None:
        self._logger.error(message)
