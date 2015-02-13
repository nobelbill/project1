__author__ = '1002097'

import sqlite3

sqlite_con =  None
database = 'comic.db'
cursor =  None
last_number_sql = "select last from comic"


def sqlite_connect() :
    try:
        sqlite_con =  sqlite3.connect(database)

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

def sqlite_disconnect() :
    try:
        if sqlite_con :
            sqlite_con.close()
    except sqlite3.Error ,e:
        print "disconnect error %s" % e.args[0]
        sys.exit(0)


def sqlite_select_last_number() :
    try:
        sqlite_connect()
        cursor = sqlite_con.cursor()
        cursor.execute(last_number_sql)
        last =  cursor.fetchone()
        print last
    except sqlite3.Error , e:
        print "select error %s" % e.args[0]


sqlite_connect()
sqlite_select_last_number()
sqlite_disconnect()
