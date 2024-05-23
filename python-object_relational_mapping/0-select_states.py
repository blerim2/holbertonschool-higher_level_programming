#!/usr/bin/python3
"""List states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """List all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
<<<<<<< HEAD
    db.close()
=======
    db.close()
>>>>>>> a7f496308a7db310cfd14d1d0b1210f239bdee61
