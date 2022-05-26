# we can run many threads but they all run in the same Process
# this means they all use the same instance of Python
# threads are parallelism within a process

from threading import Thread # this provides a thread access object
import time
import random
import sys
import timeit

# here is the function we will run as a thread
def myfunc(n):
    for i in range(1,50):
        # fifty times 0.05 is 2.5 so we expect to wait ~2.5 sec
        time.sleep( random.random()*0.1 ) # sleep for up to 01 sec
        sys.stdout.write(n) # or just print

if __name__ == '__main__':
    start = timeit.default_timer() # this starts a stop-watch
    t1 = Thread(target=myfunc, args=('t1 ',))
    t2 = Thread(target=myfunc, args=('t2 ',))
    t3 = Thread(target=myfunc, args=('t3 ',))
    t4 = Thread(target=myfunc, args=('t4 ',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join() # NB any sys.stdout will only be seen when the thread re-joins the main thread
    t2.join()
    t3.join() 
    t4.join() 

    end = timeit.default_timer() # end our stop-watch

    print('The whole thing took {} seconds'.format(end-start))
