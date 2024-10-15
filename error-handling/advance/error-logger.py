import logging
from functools import wraps


def create_logger():
    # get logger and set logging level
    logger = logging.getLogger("exec_logger")
    logger.setLevel(logging.INFO)

    # add logging file handler
    logfile = logging.FileHandler("exec_logger.log")

    # set logging formt
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)

    # add file handler and format to logger
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger


logger = create_logger()


def exception(logger):
    def decorator(func):
        @wraps(func)
        def log_runner(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except:
                issue = "exception in " + func.__name__ + "\n"
                issue = issue + "==========================" + "\n"
                logger.exception(issue)
                raise

        return log_runner

    return decorator


@exception(logger)
def divideByZero():
    return 12 / 0


# Driver Code
if __name__ == "__main__":
    divideByZero()
