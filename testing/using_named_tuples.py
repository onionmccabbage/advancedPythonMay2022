# here we explore named tuples and also pytest
from collections import namedtuple
from math import fabs

# we can use a named tuple to ensure a 'task' will have a summary, an owner, a 'done' and an id
task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# named tuples allow default values in case of absent members
task.__new__.__defaults__ = (None, None, False, None)

# we can write pytest methods to implement tests of our code
def test_defaults():
    t=task() # we hope this will use the defaults
    # s=task(None, None, True, None) # oops - not the equivalent to the defaults
    s=task(None, None, False, None)
    assert t==s # assertion fails

# pytest will look for any method beginning 'test'
def test_member_access():
    t = task('finish doing stuff', 'Grace')
    assert t.summary == 'finish doing stuff'
    assert t.owner   == 'Grace'
    assert (t.done, t.id) == (False, None)

if __name__ == '__main__':
    # t0 = task('talk about named tuples', 'td', False, 0)
    # print(t0)
    # t1 = task() # this will use the defaults
    # print(t1)
    test_defaults()
    test_member_access() ## all the test pass silently
