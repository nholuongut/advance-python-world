from threading import Thread, Lock, current_thread
import time
from queue import Queue

"""
using queue we can exchange data between threads in 
thread safe enviroment
"""


def worker(q, q_get, lock):
    while True:
        value = q.get()
        q_get.put(value)
        # with lock:
        # do some processing
        print(f"{current_thread().name} got {value}")
        time.sleep(2)
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    q_get = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, q_get, lock))
        # background threads dies when main thread dies
        thread.daemon = True
        thread.start()

    t1 = time.time()
    for i in range(1, 100):
        q.put(i)

    q.join()
    t2 = time.time()
    print(q_get.queue)
    print("time diff", t2 - t1)
    print("end main")
