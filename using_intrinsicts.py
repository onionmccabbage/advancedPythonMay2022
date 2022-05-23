# thert are many things built in to Python
# many of them are available as 'intrinsics'

class TopLevel():
    def __init__(self):
        pass # do nothing!!!

class Derived(TopLevel):
    '''this class is derived from 'TopLevel' class '''
    def __init__(self):
        super().__init__() # call the initializer of the parent class
    def __str__(self): # override how 'print' works for this class
        return 'Derived class instance'

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    # see the __str__ method
    print(d)
    # explore some intrinsic members of our class instances
    print('class name is {}'.format(Derived.__name__))
    print('class docstring is {} '.format(Derived.__doc__))
    print('class dictionary is {}'.format(Derived.__dict__))
    print('class bases are {}'.format(Derived.__bases__)) ## see the parent class
