# CONNECTION AND RETURN FUNCTION
from insert_titanic import execute_q, connection
import psycopg2

# conenction to db
pg_conn,pg_curs = connection()

#function to return result of query using execute_query from insert_titanic
# using just the connection and query
def results(pg_conn, query):
    result = execute_q(pg_conn, query)
    return result

# QUERIES 
# COUNT LEN OF DB -- 817
count = 'SELECT COUNT(*) FROM titanic'
print(results(pg_conn, count))

# NUMBER OF survived
survived = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"=1;'''
print(results(pg_conn, survived))

# NUMBER OF dead
dead = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"!=1;'''
print(results(pg_conn, dead))

# NUMBER OF dead from class 3 
dead3 = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"!=1 AND "Pclass"=3;'''
print(results(pg_conn, dead3))

# NUMBER OF survived from class 1 
survived1 = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"=1 AND "Pclass"=1;'''
print(results(pg_conn, survived1))