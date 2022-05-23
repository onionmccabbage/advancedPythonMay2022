# writing to a byte file (for efficiency)

def doWrite():
    bdata = bytes( range(0, 256) ) # 0->255
    # print(bdata)
    # persist this byte data to a file (a byte file)
    fout = open('bfile', 'wb') # 'w' will (over)write with new content. 'b' means bytes
    # 'a' to append, 'x' for exclusive access (fails if exists)
    # fout.write(bdata) # we could just write the whole lot
    # we can choose to iteratively write the output
    size = len(bdata)
    offset = 0
    chunk = 64 # here we ensure each write uses the same predictable chunk size
    while True:
        if offset > size:
            break
        fout.write( bdata[offset:offset+chunk] )
        offset += chunk
    fout.close() # always a good idea to tidy up

if __name__ == '__main__':
    doWrite()