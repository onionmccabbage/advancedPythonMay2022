import sqlite3

# write single data member to the database table
def writeDB():
    conn = sqlite3.connect('my_db') # connect to the database
    curs = conn.cursor()
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 256, 0.82)
    '''
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

if __name__ == '__main__':
    writeDB()
