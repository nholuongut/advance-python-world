# best suite for cpu intensive work
from multiprocessing import Process , Value , Array , Lock
import os
import time
from multiprocessing import Queue
from multiprocessing import Pool


def cube(number):
    return number **3

if __name__=='__main__':

    numbers = range(0,10)
    # define worker pool
    pool = Pool()

    # map , apply , join , close
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()
    print(result)