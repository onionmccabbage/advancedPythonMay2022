import socket
import sys

def myClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # match the server expectations
    # try to connect to our server
    param_t = ('localhost', 9874) # server and port
    sock.connect( param_t )
    # send a message to the server
    if len(sys.argv) > 1: # sys.argv[0] is always the module name
        msg = ' '.join(sys.argv[1:]) # leave out the first system argument variable
    else:
        msg = 'default message'
    sock.send( msg.encode() ) # all http MUST be encoded
    # handle any response from the server
    res = sock.recv(1024)
    print(res)
    sock.close() # tidy up

if __name__ == '__main__':
    myClient() # get our client up and running