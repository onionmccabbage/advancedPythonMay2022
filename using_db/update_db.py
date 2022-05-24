# here we update quantity values in the database table
import sqlite3

def updateQty():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask the user which creatue needs updating
    invalid = True
    while invalid:
        which_creature = input('Which creature needs updating? ')
        if type(which_creature)== str and len(which_creature)>0:
            invalid = False
    # ask what the quantity is
    qty = int(float(input('What is the new quantity of {} '.format(which_creature))))
    st = '''
    UPDATE zoo
    SET count = {0}
    WHERE creature IS "{1}"
    '''.format(qty, which_creature)
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

if __name__ == '__main__':
    updateQty()
