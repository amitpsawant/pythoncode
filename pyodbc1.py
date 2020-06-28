import pyodbc
import json

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select name from site")
    for row in cursor:
        print(f'row = {row}')
    print ("%s, " % (row[0]))

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=.;"
    "Database=aqm20;"
    "Trusted_Connection=yes;"
)

read(conn)
