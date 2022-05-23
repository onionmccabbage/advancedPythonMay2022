# Python uses the @ sign to indicate a 'decorator'
# in addition to bniuld-in decoartors such as @property we can write our own custom decorator

# we will write a decorator
# this decorator will display all the parameters passed in to any function
def show_args(func): # here we pass a function into our function
    def my_fn(*args, **kwargs):
        # we can print info about the passed-in function
        print('Running a function called {}'.format(func.__name__))
        print('Positional arguments are {}'.format(args))
        print('Keyword arguments are {}'.format(kwargs))
        # then we run the passed-in function
        return func(*args, **kwargs)
    return my_fn # here we return the original function WITHOUT calling it again

# ..and we will write a simple function  to be decorated
@show_args # we decorate our function with our custom decorator
def add_ints(a, b):
    '''return the sum of two integer values'''
    if isinstance(a, int) and isinstance(b, int):
        # all good we can add them together
        return a+b
    else:
        # we can decide what to do if they are not integers
        return 'non-integers provided'

# it is good practice to use the if __name__ == '__main__' syntax
if __name__ == '__main__':
    # this code will only run if this is the main module
    # this code will lNOT run if this module has been imported elsewhere
    x, y = [1, 2] # unpack a list
    print(add_ints(x, y)) # pass in only positional arguments (NB tuple of positional arguments)
    print(add_ints(a=3, b=4)) # pass in oly keyword arguments (NB a dict of keyword arguments)
    print(add_ints(6, b=2)) # pass in one positional argument and one keyword argument
