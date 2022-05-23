# Python uses generators and comprehension
r = range(1, 20, 2) # start, stop-before, step
# we can make a generator from this range
g = (i*i for i in r) # this makes a generator object
l = [i**0.5 for i in r] # this makes a list (persistant in memory)
# print(g)

# we can write a custom generator. A generator is like a normal function but with 'yield' in place of 'return'
def byteGen(start, stop_before):
    '''generate byte values between supplied parameters'''
    s = start # so we can incrementt the value
    while s < stop_before:
        # NB yield will supply the __next__value each time the generator is called
        yield bytes(s) # take the value 's' and convert to bytes
        s+=1

if __name__ == '__main__':
    # we need an instance of our custom generator
    b = byteGen(70, 88)
    for v in g:
        print(v, end=', ')
    for v in l:
        print(v, end=', ')
    # we can call our generator to yield each value
    print(b.__next__())
    print(b.__next__())
    print(b.__next__())
    
    # for v in b:
    #     print(v, end=', ') # we get a load of byte-encoded data