# best suite for cpu intensive work
from multiprocessing import Process , Value , Array , Lock
import os
import time
from multiprocessing import Queue
import numpy as np

# since processors not live inside same memeory global variables don't work

# def add_100(number,lock):

#     for i in range(100):
#         time.sleep(0.01)
#         # prevent multiple processors update shared number same time
#         with lock :
#             #lock.acquire()
#             number.value += 1
#             #lock.release()


def add_100(array,lock):

    for i in range(100):
        time.sleep(0.01)
        # prevent multiple processors update shared number same time
        with lock :
            for i in range(len(array)):
                array[i] += 1 #np.random.randint(0,10)

if __name__=='__main__':

    # define the process lock
    lock = Lock()
    shared_number = Value('i', 0)   
    shared_array = Array('d',[0.0 , 100.0 , 200.0])
    print("array at begining : ", shared_array[:] )

    #p1 = Process(target=add_100, args=(shared_number,lock))
    #p2 = Process(target=add_100 , args=(shared_number,lock))

    p1 = Process(target=add_100, args=(shared_array,lock))
    p2 = Process(target=add_100 , args=(shared_array,lock))

    p1.start()
    p2.start()

    # wait till complete
    p1.join()
    p2.join()

    print("end array :", shared_array[:])