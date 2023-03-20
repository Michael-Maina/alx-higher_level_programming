#!/usr/bin/python3
"""
script that takes in an argument and displays all values in \
the states table of hbtn_0e_0_usa where name matches the argument \
and is safe from MySQL injections.
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    if len(argv[4]) <= 12:
        cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
                     ORDER BY id ASC".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    cur.close()
    conn.close()
