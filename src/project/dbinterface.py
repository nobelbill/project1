__author__ = '1002097'

import sqlite3

sqlite_con =  None
database = 'comic.db'
cursor =  None
last_number_sql = "select last from comit"


def sqlite_connect() :
    try:
        sqlite_con = sqlite3.connect(database)
        print "sqlite connect"
        return  sqlite_con
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

def sqlite_disconnect(con) :
    try:
        if con :
            con.close()
        print "sqlite disconnect"
    except sqlite3.Error ,e:
        print "disconnect error %s" % e.args[0]
        sys.exit(0)


def sqlite_select_last_number() :
    try:
        con = sqlite_connect()
        cursor = con.cursor()
        cursor.execute(last_number_sql)
        last =  cursor.fetchone()
        print last
        sqlite_disconnect(con)
    except sqlite3.Error , e:
        print "select error %s" % e.args[0]


sqlite_select_last_number()
