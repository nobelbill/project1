__author__ = '1002097'

import sqlite3

sqlite_con =  None
database = 'comic.db'

def sqlite_connect() :
    try:
        sqlite_con =  sqlite3.connect(database)

        cursor = sqlite_con.cursor()
        cursor.execute('select sqlite_version()')
        data = cursor.fetchone()

        print "version %s" % data

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if sqlite_con:
            sqlite_con.close()

sqlite_connect()
