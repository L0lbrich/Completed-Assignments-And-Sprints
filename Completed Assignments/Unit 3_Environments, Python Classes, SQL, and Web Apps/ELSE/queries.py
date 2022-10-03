#302 characters
GET_CHARACTERS = 'SELECT * FROM Charactercreator_characters;'

# query to make a table called test

create_test_table = '''CREATE TABLE test_table 
                        ("id" SERIAL NOT NULL PRIMARY KEY, 
                        "name" VARCHAR(30) NOT NULL,
                        "age" INT NOT NULL);'''

insert_test_table = '''INSERT INTO test_table ("name", "age")
                    VALUES ('Logan O',23);'''
                
drop_table = '''DROP TABLE IF EXISTS characters'''

get_test_table = '''SELECT * FROM test_table'''

create_table_character = ''' CREATE TABLE IF NOT EXISTS characters
                            ("character_id" SERIAL NOT NULL PRIMARY KEY,
                            "name" VARCHAR(30) NOT NULL,
                            "level" INT NOT NULL,
                            "exp" INT NOT NULL,
                            "hp" INT NOT NULL,
                            "strength" INT NOT NULL,
                            "intelligence" INT NOT NULL,
                            "dexterity" INT NOT NULL,
                            "wisdom" INT NOT NULL);
                            '''
insert_logan = '''INSERT INTO characters ("name","level","exp","hp","strength","intelligence","dexterity","wisdom")
                VALUES ('Logan O',50,100,1000,15000,6,80,2134)'''

