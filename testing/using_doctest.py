# doctest lets us write unit tests within the docstring
import doctest

def nthpower(d, p):
    '''
    Return the nth power of a number
    We can write doctests within the doc string
    >>> nthpower(4,3)
    64
    >>> nthpower(1, 1)
    1
    '''
    return d**p

def cubeIt(a, b):
    '''
    return all the cubes of numbers from a to b
    >>> cubeIt(3, 8)
    [27, 64, 125, 216, 343, 512]
    >>> cubeIt(1, 10) # doctest:+ELLIPSIS
    [1, 8, ..., 1000]
    '''
    answers = []
    for i in range(a, b+1):
        answers.append( i**3 )
    return answers

if __name__ == '__main__':
    # print( nthpower(4, 3) )
    doctest.testmod(verbose=True) # always show full test outcome
    # print( cubeIt(-5, 5) )