from api import data
import sqlite3 
from sqlite3 import Error
from datetime import datetime
import os

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

    return conn


 
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)

def create_questions(conn, questions):
    sql = '''
            INSERT INTO questions(question_number, question, creation_date)
            VALUES(?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql, questions)
    conn.commit()
    return cur.lastrowid


# END OF MAKING THE FUNCTIONS
# THIS IS MAIN

dir_path = os.path.dirname(os.path.realpath(__file__))
database = dir_path + "/Questions.db"


sql_create_projects_table = """
                                CREATE TABLE IF NOT EXISTS questions (
                                    id integer PRIMARY KEY,
                                    question_number interger NOT NULL,
                                    question text NOT NULL, 
                                    creation_date text
                                );
"""

conn  = create_connection(database)



if conn is not None:
    create_table(conn, sql_create_projects_table)

else:
    print("ERROR! CANT CONNECT.")

with conn:
    for keys, values in data.items():
        current_time = (datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
        print(values)
        question = (keys, str(values), current_time)
        question_id = create_questions(conn, question)

