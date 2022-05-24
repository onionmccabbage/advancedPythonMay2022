# here we will populate our databasee with many creatures
# we will use secure mechanisms to inject data
import sqlite3

def populateDB():
    '''
    Here we pass parameters to the database for each new creature
    '''
    creatures_t = ( # we would normally get the value from the user, from a config file or from an API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )
    # we need a connection and a cursor
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we will use ? to inject parameters into our statement
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures_t:
        try:
            # we should check the vaules being inserted are safe (sanitize the data)
            if type(item['creature']) == str and item['creature'] != '':
                n = item['creature']
            else:
                raise Exception
            if type(item['count']) == int and item['count'] >=0:
                c = item['count']
            else:
                raise Exception
            if type(item['cost'])== float and item['cost'] >=0:
                co = item['cost']
            else:
                raise Exception
            # use the values to execute the cursor statement
            curs.execute(st, (n, c, co)) # the order matters
            conn.commit() # make sure the changes persist in the database
        except Exception as err:
            print('SQL injection problem: {}'.format(err))
    # after the loop completes we will tidy up
    conn.close()

if __name__ == '__main__':
    populateDB()
