# here we will populate our databasee with many creatures
# we will use secure mechanisms to inject data
import sqlite3

def custom_insertDB():
    '''
    Here we ask the user for values to insert into the database
    '''
    invalid_name = True
    invalid_count = True
    invalid_cost = True
    while invalid_name:
        creature_name = input('Creature name? ')
        if type(creature_name)==str and len(creature_name) >0:
            invalid_name = False
    while invalid_count:
        count = int( float(input('How many {}? '.format(creature_name))))
        if type(count)==int and count >=0:
            invalid_count = False    
    while invalid_cost:
        cost = float(input('Cost of each {}? '.format(creature_name)))
        if type(cost)==float and cost >=0:
            invalid_cost = False

    # we need a connection and a cursor
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we will use ? to inject parameters into our statement
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    try:
        # we should check the vaules being inserted are safe (sanitize the data)
        if type(creature_name) == str and creature_name != '':
            n = creature_name
        else:
            raise Exception
        if type(count) == int and count>=0:
            c = count
        else:
            raise Exception
        if type(cost)== float and cost >=0:
            co = cost
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
    custom_insertDB()
