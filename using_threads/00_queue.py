import queue
import threading
import time # not from time import time

dish_queue = queue.Queue() # this queue is globally available to everythnig in this Python module

def washer(dishes,dish_queue):
    for dish in dishes:
        print('Washing {}'.format(dish))
        time.sleep(0.5)
        dish_queue.put(dish) # the queue wil grow as items aree placed on it

def dryer(dish_queue):
    while True: # careful - this thread will run endlessly
        dish = dish_queue.get() # grab the next available item off the queue
        if dish == None:
            print('cant try None!!!')
            quit
        print('Drying {}'.format(dish))
        time.sleep(0.8) # we emulate some long-running operation by sleeping
        # this next line tells Python t move on. It is not needed but best practice
        dish_queue.task_done() # this loop of the 'while' operator will end

if __name__ == '__main__':
    dishes = ['salad', 'bread', 'entree', 'desert', None]
    for n in range(2):
        # here we target any old function, which we wish to run on a thread
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,)) # args as a tuple
        dryer_thread.start() # now our dryer function will begin running on a new thread
        # dryer_thread.join() # not a good idea to 'join' a thead that has an endless loop
        # we now have many threads - how can we 'join' them all back again
    washer(dishes, dish_queue) # pass in the gloabl variable
    # it is good practice to explicitly 'join' a thread back to the main thread
    dryer_thread.join() # NB queue is (internally) threaded already
    dish_queue.join() # NB queue is (internally) threaded already