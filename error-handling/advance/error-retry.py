from functools import wraps
import time


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """

    def deco_retry(f):
        @wraps(f)
        def call_retry(*args, **kwargs):
            mtries, mdelay = tries, delay

            # iterate till max trials
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    error_msg = f"Error : {e} Retrying in {mdelay}s ...."

                    # log message if logger provided
                    if logger:
                        logger.warning(error_msg)
                    else:
                        print(error_msg)

                    # add sleep
                    time.sleep(mdelay)

                    # increment delay by backoff multiplier
                    mdelay = mdelay * backoff
                    mtries -= 1

            return f(*args, **kwargs)

        return call_retry

    return deco_retry


@retry(Exception, tries=4)
def ping_server(text):
    raise Exception("Fail .")


ping_server("Working ...")
