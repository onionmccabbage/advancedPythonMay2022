# we may need to pip install memory_profiler
from memory_profiler import profile
import collections

# we can use a double-ended queue which allows add/remove to BOTH ends
def someFn():
    my_deq = collections.deque('98765432')
    # we can acces both ends of the queue
    my_deq.append('1') # '987654321
    my_deq.appendleft(0) # '0987654321'
    my_deq.pop()
    my_deq.popleft()
    print('Deque {} type{}'.format(my_deq, type(my_deq)))

@profile # we can decorate any function to get a memory profile
def main():
    someFn()

if __name__ == '__main__':
    main()