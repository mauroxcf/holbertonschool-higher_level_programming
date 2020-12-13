#!/usr/bin/python3
""" script that lists all cities from the database """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # connect to mysql, passing 4 arguments in argv
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306,
                         charset="utf8")

    # cursor object
    cur_obj = db.cursor()

    # select the query
    cur_obj.execute("SELECT cities.name FROM cities\
                     INNER JOIN states ON cities.state_id\
                          = states.id WHERE states.name =%s", [argv[4]])

    myresult = cur_obj.fetchall()

    temp = ""
    for i in myresult:
        temp += str(*i) if temp == "" else ", " + str(*i)
    print(temp)

    # close cursor
    cur_obj.close()

    # close database
    db.close()
