import sys

class Redirect:
    '''
    This class allows redirection of content to another output stream
    The original contet is returned when done
    '''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    def __enter__(self): # override the built in __enter__ method
        '''
        The __enter__ method is invoked whenever an instance of this class is invoked
        Also if this class is directly invoked
        '''
        self.orig_stdout = sys.stdout  # make a note of the current output stream
        sys.stdout = self.new_stdout # redirect output to whtever was passed in
    def __exit__(self, exc_type, exc_value, exc_traceback): # this must accept all these arguments
        sys.stdout = self.orig_stdout # reset the oyutput stream back to the original


if __name__ == '__main__':
    print('current output is {}'.format(sys.stdout))
    with open('my_log.txt', 'a') as fobj:
        with Redirect(fobj): # here we are invoking hte actual Redirect class (we could do the same with an instance)
            print('this gets written to our log file')
            print('because the output stream is now {}'.format(sys.stdout))
        print('Output has been restored to {}'.format(sys.stdout))
