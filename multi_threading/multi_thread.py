from threading import Thread, Lock, current_thread
import time

database_value = 0


# add lock method to update global variable sequentially
def increase(lock):
    global database_value
    # lock certain process until complete other threads will not execute until lock release
    print(f"{current_thread().name }")
    with lock:
        print(f"{current_thread().name } lock acquired  ")
        for i in range(10):
            database_value += 1**10
        print("done")
    time.sleep(3)


if __name__ == "__main__":
    lock = Lock()
    print("start value : ", database_value)

    # define two threads
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    t1 = time.time()
    # start two threads
    thread1.start()
    thread2.start()

    # wait for the threads
    thread1.join()
    thread2.join()

    # main thread
    print("end value : ", database_value)
    print("time gap ", time.time() - t1)
