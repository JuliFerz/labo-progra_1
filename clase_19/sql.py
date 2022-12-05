import sqlite3
from constantes import *

class Sql:
    @staticmethod
    def create_table():
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                query = ''' CREATE TABLE "score" (
                            "id"	INTEGER NOT NULL,
                            "name"	TEXT NOT NULL,
                            "score"	INTEGER NOT NULL,
                            "time"	INTEGER NOT NULL,
                            PRIMARY KEY("id" AUTOINCREMENT)
                            )
                        '''
                connection.execute(query)
                print('✅ Table created')
            except sqlite3.OperationalError:
                print('❌ Table already exist')


    @staticmethod
    def eliminate_table(table):
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                query = f' DROP TABLE {table}'
                connection.execute(query)
                print('✅ Table eliminated')
            except sqlite3.OperationalError:
                print('❌ Error')


    @staticmethod
    def create_record(name, score, time):
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                connection.execute(''' INSERT INTO score(name,score,time)
                                    VALUES (?,?,?)''',
                                    (name,score,time))
                connection.commit()
                print('✅ Record created')
            except sqlite3.OperationalError:
                print('❌ Error')

    @staticmethod
    def select_all_record():
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                cursor = connection.execute(''' SELECT * 
                                                FROM score
                                            ''')
                return cursor
            except sqlite3.OperationalError:
                print('❌ Error')

    @staticmethod
    def select_where_record():
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                query = ('''SELECT * 
                            FROM score
                            WHERE time < ?
                        ''')
                cursor=connection.execute(query, (100,))
                # for fila in cursor:
                    # print(fila) 
            except sqlite3.OperationalError:
                print('❌ Error')
            
    @staticmethod
    def delete_table_where(id):
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                query = ('''DELETE FROM score 
                            WHERE id=?
                        ''')
                cursor=connection.execute(query, (id,))
                print('✅ Campo eliminado')
            except sqlite3.OperationalError:
                print('❌ Error')

    @staticmethod
    def update_table_where():
        with sqlite3.connect(f'{PATH_DB}/pygame_database.db') as connection:
            try:
                query = ('''   UPDATE score 
                                SET score=?
                                WHERE id=?
                        ''')
                cursor=connection.execute(query, (100,3,))
                filas=cursor.fetchall()
                # for fila in filas:
                    # print(fila)
            except sqlite3.OperationalError:
                print('❌ Error')
    