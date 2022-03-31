#step 0 import sqlite3
#also get the database file into the folder where were working
import sqlite3
import queries

#step 1 connect to the database
connection = sqlite3.connect('rpg_db.sqlite3')

#step 2 - create cursor
cursor = connection.cursor()

#step 3 - write a query
query = 'SELECT * FROM charactercreator_character;'

# DB Connect    
def connect_db(name='rpg_db.sqlite3'):
    return sqlite3.connect(name)

# cursor execute query function
def execute_q(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ensure that the queries are only being run when 
# the files is executed as a script
# `python sqlite_example.py`
if __name__ == '__main__':
    #step 4 - Execute the query on the cursor not on the connection
    #cursor.execute(query)
    
    #step 5 - fetch the results from the cursor
    #results = cursor.fetchall()
    #print(results[:5])  
    
    
    #results from queries.py file and db_connect/cursor execute functions w/ select_all variable
    conn = connect_db()
    results = execute_q(conn, queries.items_per_char)
    print(results[:5])
    
    