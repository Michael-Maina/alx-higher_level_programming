#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all \
cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    if len(argv[4]) <= 12:
        cur.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    WHERE states.name = '{}'\
                    ORDER BY cities.id ASC".format(argv[4]))
        rows = cur.fetchall()
        cities = ", ".join(row[0] for row in rows)
        print(cities)
    cur.close()
    conn.close()
