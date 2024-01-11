#!/usr/bin/python3
# Import MySQLdb module
import MySQLdb
# Import sys module to get command-line arguments
import sys

# Get the username, password, and database name from the arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server on localhost at port 3306
connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Create a cursor object
cursor = connection.cursor()

# Execute the SQL query to select all states ordered by id
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the results from the cursor
results = cursor.fetchall()

# Loop through the results and print each one
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()
