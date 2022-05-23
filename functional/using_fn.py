# instead of using classes many coding solutions only need purely functional code

# some simple functions
from functools import reduce # 'functools' is built in to Python
def squareIt(x):
    '''return the square of a number'''
    return x*x

def addThem(x, y):
    '''return the two values added together'''
    return x+y

def isOdd(n):
    '''return True or Falee depending on if the value is Odd or Even'''
    return n%2 !=0

if __name__ == '__main__':
    # suppose we need a list of square numbers in a range. We can map all teh valuesd into our 'squareIt' function
    sq_l = ( map(squareIt, range(1, 12)) ) # this is a map object (a generator)
    print( sq_l.__next__() ) # we can grab each value in turn
    print( sq_l.__next__() ) # 
    print( sq_l.__next__() ) # eventually our 'map' wiull be exhausted and yield no further values
    # we can yield all the values into a collection
    squares_list = list(sq_l) # just the remaining values
    print(squares_list)
    # similarly we can use 'filter' to pass a load of values to a filter function 
    odd_l = ( filter( isOdd, range(1, 27) ) )
    print(odd_l.__next__()) # it is a filter object, i.e. a generator
    print(odd_l.__next__()) 
    print(odd_l.__next__()) 
    print(odd_l.__next__()) 
    # we can choose to persist the generated values, e.g. in a tuple or a list etc
    odd_t = tuple(odd_l)
    print(odd_t)
    # there is also a 'reduce' method (needs to be imported)
    # 'reduce' will iteratively apply a function to end up with a single value
    r = reduce( addThem, odd_t ) # iteratively add each member of the odd tuple
    print(r)