'''
Created on Dec 14, 2018

@author: p636205
'''
# https://wiki.python.org/moin/Concurrency/
# https://talkpython.fm/episodes/show/58/create-better-python-programs-with-concurrency-libraries-and-patterns
# https://doc.lagout.org/programmation/python/Python%20in%20Practice_%20Create%20Better%20Programs%20using%20Concurrency%2C%20Libraries%2C%20and%20Patterns%20%5BSummerfield%202013-08-29%5D.pdf

import threading
from multiprocessing import Lock, Process

def countdown():
    x = 1000000000
    while x > 0:
        x -= 1

def countdown2():
    mutex = Lock()
    with mutex:
        x = 1000000000
        while x > 0:
            x -= 1
         
# Implementation 1: Multi-threading
def implementation_1():
    thread_1 = threading.Thread(target=countdown)
    thread_2 = threading.Thread(target=countdown)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
# Implementation 2: Run in serial
def implementation_2():
    countdown()
    countdown()




# countdown() is defined in the previous snippet.
def implementation_3():
    process_1 = Process(target=countdown)
    process_2 = Process(target=countdown)
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    
def implementation_4():
    process_1 = Process(target=countdown2)
    process_2 = Process(target=countdown2)
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()

if __name__ == '__main__':
    import time
    start_time = time.time()
    print("threading")
    implementation_1()
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("concurrent")
    implementation_2()
    print("--- %s seconds ---" % (time.time() - start_time))
    ## Serial beats multi threaded due to Global Interpreter Lock (GIL)
    start_time = time.time()
    print("multiprocessing without mutex")
    implementation_3()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("multiprocessing with mutex")
    implementation_4()
    print("--- %s seconds ---" % (time.time() - start_time))
    ## Serial beats multi threaded due to Global Interpreter Lock (GIL)
    ## Multiprocessing uses more resources but inhabits different memory spaces
    ## and is concurrent in the way I might expect
    ## Threading is okay for IO calls
    # mutex introduced in multiprocessing slowed it down, of course
    #    call a process with args     p = Process(target = processData, args = (some_data,))
