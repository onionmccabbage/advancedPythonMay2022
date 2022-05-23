# we can use our decorator anywhere
from using_decorators import show_args

@show_args
def trivial(a, b, c):
    return (a-b)**c

if __name__ == '__main__':
    print( trivial(3,2,1) )
    print( trivial(3,2,c=1) )