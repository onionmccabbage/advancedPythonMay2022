# Python has a context manager
import sys
from contextlib import contextmanager

@contextmanager # make this function able to manage contexts
def stdout_redirect(new_stdout):
    '''
    this function can redirect output to a different stream
    It will then return output t the original stream
    '''
    save_stdout = sys.stdout # grab whatever is the current output 
    sys.stdout = new_stdout # set a new output
    yield # this will yield the next available object to be written to the output stream
    sys.stdout = save_stdout # return the output to what is was before

if __name__ == '__main__':
    with open('my_log.txt', 'a') as fobj: # we now have a file access object
        with stdout_redirect(fobj):
            #we can write many lines
            print('''Here are several lines we will capture
They all end up in our log file
Each is redirected by our context managing function''')
            print('This text also gets yields to the file access object')
        # when the 'with' ends, the file access will close
        print('back to the normal stdout (terminal)')