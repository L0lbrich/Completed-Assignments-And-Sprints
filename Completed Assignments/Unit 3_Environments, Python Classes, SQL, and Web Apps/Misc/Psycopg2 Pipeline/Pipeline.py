# Using Psycopg2.connect to connect to a database using PostgreSQL
import psycopg2
import sqlite3
import queries as q
#POSTGRES CONNECTION CREDENTIALS (DONT PUSH TO GITHUB)
DBNAME = 'pzmmufbp'
USER = 'pzmmufbp'
PASSWORD = 'xgqS-FE8BW1iprF2FtlH1ckuCQH2iukF' 
HOST = 'kashin.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=DBNAME,
                            user=USER, 
                            password=PASSWORD,
                            host=HOST)
pg_curs = pg_conn.cursor()

# SQLite connection
sl_conn = sqlite3.connect(database='rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

def modify_table(curs, conn, query):
    curs.execute(query)
    conn.commit()

def query_table(curs,conn,query):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()

if __name__ == '__main__':
    #pg_curs.execute(q.create_test_table)
    #pg_curs.execute(q.insert_test_table)
    #modify_table(pg_curs,pg_conn,q.create_table_character)
    #modify_table(pg_curs,pg_conn,q.insert_logan)

    sl_characters = query_table(sl_curs, sl_conn, q.GET_CHARACTERS)
    for character in sl_characters[:5]:
       modify_table(pg_curs,pg_conn, f'''INSERT INTO characters ("name","level","exp","hp","strength","intelligence","dexterity","wisdom")
                VALUES ('{character[1]}',{character[2]},{character[3]},{character[4]},{character[5]},{character[6]},{character[7]},{character[8]})''')

    