#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ('''Opened database successfully''')

conn.execute('''create table if not exists COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ('''Table created successfully''')

conn.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';''')

conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
    VALUES (1, 'Paul', 32, 'California', 20000.00 )''')

conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
    VALUES (2, 'Allen', 25, 'Texas', 15000.00 )''')

conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
    VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )''')

conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
    VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )''')

insert = conn.execute("SELECT id, name, address, salary from COMPANY")

print()
for i in insert:
    print(i)

conn.close()