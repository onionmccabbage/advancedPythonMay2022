# ways to pass aruments into funtions

def fnA(*args): # positional arguments are gathered together into a tuple
    print(args) # we could access any positonal argument within this tuple

def fnB(**kwargs): # key-word arguments are gathered together into a dictionary
    print(kwargs)

def fnC(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    fnA(1, True, [], {}, (3,2,1)) # these arguments have ordinal positions
    fnB(w=False, x=(4,3,2), z=9, y=[]) # these arguments are identified by keywords
    fnC('hello', [], (1,), c={}, other=fnA)