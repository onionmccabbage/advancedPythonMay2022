# in all flavours of Pythno that are writen in C there is a global Interpreter Lock (GIL)
# This degrades thread performance
# we can take control of locks ourselves
from threading import Lock
import time, random, sys

def main():
    lock = Lock() # creat an instance of the Lock class
    # lock.acquire()
    # try:
    #     for i in range(1,50):
    #         time.sleep(random.random()*0.1)
    #         sys.stdout.write('{}'.format(i))
    # except Exception as err:
    #     print(err)
    # finally:
    #     lock.release() # tidy up
    # alternative syntax
    with lock:
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write('{}'.format(i))
    # no need to release the lock, it will be released when the 'with' ends

if __name__ == '__main__':
    main()