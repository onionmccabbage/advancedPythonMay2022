import sqlite3 # built in to Python (we can use any DB engine)

# make a coonectionto a database
def accessDB():
    '''
    This database will manage Zoo creatures
    Each creature has a creature-name (varchar) count (int) and cost (float)
    the primary key will be creature-name
    '''
    conn = sqlite3.connect('my_db') # connect or create the database
    # we need a cursor to interact with the database
    curs = conn.cursor()
    # now we can define the structure of a database table
    # this is done with an SQL statement (this is the structured query language)
    st = '''
    CREATE TABLE zoo 
    (
        creature VARCHAR(32) PRIMARY KEY,
        count INT,
        cost FLOAT
    )
    '''
    # we can execute this statement
    curs.execute(st) # this should be in a try-except block
    conn.commit()
    conn.close() # always close as soon as you can rather than leave resources unused

if __name__ == '__main__':
    accessDB()

# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip isntasll first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")