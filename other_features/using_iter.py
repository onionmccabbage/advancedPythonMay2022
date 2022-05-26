# iter is built in to python
l = [False, 7, 'text', (5,4,3,2)] # list
l_iter = iter(l) # we now have an iterable from our list

print( l_iter.__next__() ) # we could not call __next__ on a list
print( l_iter.__next__() )
print( l_iter.__next__() )
print( l_iter.__next__() )