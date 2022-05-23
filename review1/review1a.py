from my_decorators import show_args
from my_decorators import show_intrinsics

def root(x):
    return x**0.5 # anything to the power of 0.5 is the square root

@show_intrinsics
def mapRoots(start, number):
    '''
    Return the square root of integers between min and max
    '''
    print('Using Map')
    # roots = map(lambda x: x**0.5, range(start,number+1))
    roots = list( map(root, range(start,number+1)) )
    print(roots)

def compRoots(start, number):
    print('Using List comprehension')
    roots = [x**0.5 for x in range(start,number+1)]
    for root in roots:
        print (root)

def genRoots(start, number):
    print('Using Generator comprehension')
    roots = (x**0.5 for x in range(start,number+1))
    for root in roots:
        print (root)

if __name__ == '__main__':
    number = 0
    while number<1:
        number = int(float(input('Enter number : ')))
    start = 0
    mapRoots(start, number)
    compRoots(start, number)
    genRoots(start, number)
