import multiprocessing
from multiprocessing import Process
from threading import Thread

import  time

# Create a new process with specific function to execute with args.
def example(args):
    print(args)

def run_async(function, *args):
    t = time.time()
    # p = Process(target=function, args=args)
    # p.start()
    function(*args)
    # print(p.exitcode)
    print(time.time() - t)


def run_thread(function, *args):
    t = Thread(target=function, args=args)
    t.start()