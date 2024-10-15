# best suite for cpu intensive work
from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start the process
for p in processes:
    p.start()

# block main process until others completed
for i_process in processes:
    i_process.join()

print("Done")