from threading import Thread
import random
import time
import sys
import timeit # the timeit tool is a better timer than the 'time' library

class MyClass(Thread): # we inherit from the Thread class, so our class is a thread
    def __init__(self, n):
        Thread.__init__(self) # call the parent inititializer
        self.n = n # we could use 'get' and 'set'
    def doStuff(self):
        for i in range(1,50):
            time.sleep(random.random()*0.1) # about 2.5 seconds in all
            sys.stdout.write(self.n)
    # here we override the 'run' method of the Thread class
    def run(self):
        self.doStuff() # called when this thread starts

# Alternative way to run class as a thread
class Other: # this is NOT a thread
    def __call__(self, n): # threads can target ANY class that includes a __call__ method
        for i in range(1,50):
            time.sleep(random.random()*0.1) # about 2.5 seconds in all
            sys.stdout.write(n) # careful - we are not being thread-safe so the output may be corrupted
        
if __name__ == '__main__':

    # iteratively create a bunch of thread-access objects
    t_l = []
    for i in range(1,10): # by 1000 threads we get some odd behaviour, probably due to the GIL
        t_l.append(MyClass('m{} '.format(i)))
    start = timeit.default_timer()
    for task in t_l:
        task.start()
    for task in t_l:
        task.join()
    # m1 = MyClass('m1 ') # instance of our runnable class
    # m2 = MyClass('m2 ')
    # m3 = MyClass('m3 ')
    # m4 = MyClass('m4 ')
    # o = Other() # this is not a Thread instance. This instance exists in the main context
    # ot = Thread(target=o, args=('ot ',)) # remember args is a TUPLE
    # m1.start()
    # m2.start()
    # m3.start()
    # m4.start()
    # ot.start() # the RUN of this instance happens on a new thread
    # m1.join()
    # m2.join()
    # m3.join()
    # m4.join()
    # ot.join()

    end = timeit.default_timer()

    print('overall time was {}'.format(end-start))