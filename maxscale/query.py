#!/usr/bin/env python3 
import mariadb
import sys

# Connect to MariaDB Platform https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
try:
    conn1 = mariadb.connect(
        user="maxuser",
        password="maxpwd",
        host="127.0.0.1",
        port=4000,

    )

    conn2 = mariadb.connect(
        user="maxuser",
        password="maxpwd",
        host="127.0.0.1",
        port=4000,

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur1 = conn1.cursor()
cur2 = conn2.cursor()

cur1.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10")

cur2.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")


print('The last 10 rows from zipcodes_one')
result1 = cur1.fetchall()
for row in result1:
    print (row)


print('The first 10 rows from zipcodes_two')
result2 = cur2.fetchall()
for row in result2:
    print (row)

print('The largest zipcode from zipcodes_one')
cur1.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY zipcode DESC LIMIT 1")
result3 = cur1.fetchall()
print(result3)

print('The smallest zipcode from zipcodes_two')
cur2.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY zipcode LIMIT 1")
result4 = cur2.fetchall()
print(result4)

conn1.close()
conn2.close()
