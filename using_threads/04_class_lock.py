from threading import Thread, Lock

lock = Lock()
count1 = 0
count2 = 0

class MyClass():
    def __call__(self, name):
        global lock, count1, count2
        # we can manage count2 with our own lock
        lock.acquire()
        for i in range(0,20):
            count2 += 1
            print('count2 is {}'.format(count2))  
        lock.release()      
        for i in range(0,20): # let the GIL manage shared memory locking
            count1 += 1
            print('count1 is {}'.format(count1))

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('t1 ',))
    t2 = Thread(target=m2, args=('t2 ',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(count1, count2)