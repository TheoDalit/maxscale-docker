#!/usr/bin/env python3 
import mariadb
import sys

# Connect to MariaDB Platform https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
try:
    conn = mariadb.connect(
        user="maxuser",
        password="maxpwd",
        host="127.0.0.1",
        port=4000,
        database="zipcodes_one"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

z1 = "SELECT * FROM zipcodes_one.zipcodes_one"
z2 = "SELECT * FROM zipcodes_two.zipcodes_two"

cur.execute(z1)
cur.execute(z2)

result = cur.fetchall()
for row in result:
    print (row)

conn.close()
