#!/usr/bin/env python

from threading import Thread, Lock
import random
import time

stdout_lock = Lock()

start_time = time.time()

class SimpleThread(Thread):
    def __init__(self, num):
        super().__init__()  # Thread.__init__(self)
        self._threadnum = num

    def run(self):  # <2>
        time.sleep(random.randint(1, 3))
        with stdout_lock:
            print("Hello from thread {}".format(self._threadnum))


all_threads = []
for i in range(10):
    t = SimpleThread(i)  # <3>
    t.start()  # <4>
    all_threads.append(t)

print("Done.")

for t in all_threads:
    t.join()  # wait for thread to finish

print(f"Program took {time.time() - start_time} seconds")




