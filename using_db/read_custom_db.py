import sqlite3

def readDB():
    # ask the user which creature to see
    whichCreature = input('Which creature? ')
    conn = sqlite3.connect('my_db') # connect to the database
    curs = conn.cursor()
    st = '''
        SELECT creature, count, cost FROM zoo
        WHERE creature LIKE "%{}%"
        ORDER BY count DESC
    ''' .format(whichCreature)
    try:
        curs.execute(st)
        # now we can use our cursor to fetch data
        rows = curs.fetchall()
    except Exception as err:
        print(err)
    finally:
        conn.close()
    # we can explore the returned data rows
    # print(rows) # a list of tuples (each row is retuned as a tuple)
    # we can iterate over the returned rows
    for animal in rows:
        print('we have {1} {0} each costing {2:0.2f}'.format(animal[0], animal[1], animal[2]))

if __name__ == '__main__':
    readDB()