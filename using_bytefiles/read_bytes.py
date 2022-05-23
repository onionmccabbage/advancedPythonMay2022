# reading the byte file back in again

def doRead():
    fin = open('bfile', 'rb') # read bytes
    bdata = fin.read() # could chunk it into parts
    print(bdata)
    fin.close()
    s = str(bdata) # convert the bytes into string
    print(s)


if __name__ == '__main__':
    doRead()