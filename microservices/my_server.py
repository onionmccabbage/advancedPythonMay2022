import socket

def myServer():
    '''
    This service will echo any request back to the client
    (having first capitalised the request body)
    '''
    # here are the most common socket parameters
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874) # server and port
    server.bind(param_t) # set our server parameters
    # begin listening for requests
    server.listen(4) # handle up to four concurrent requests (or queue them if busy)
    print('This server is listening on port {} on {}'.format(param_t[1], param_t[0]))
    while True: # keep our server running
        # when a request is made, we need to handle it
        (client, addr) = server.accept() # unpack the request
        print(client,addr)
        # read any data received from the client
        buf = client.recv(1024) # read just the first 1024 bytes from the client
        print('Server received {}'.format(buf))
        # decide what to do about this request  -in this case capitalise and echo back to client
        resp = buf.upper()
        client.send(resp)
        # we need a way to quit the server
        if buf == b'quit': # bytes version of the word 'quit'
            server.close()
            break # end our run loop

if __name__ == '__main__':
    myServer() # invoke our server