import sqlite3
import sqlite3
from sqlite3 import Error
from pydocx import PyDocX
import os
import base64
from pydocx.export import base



def create_connection(db_file):
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        return conn
    
    except Error as e:
        print(e)

    return conn




def fetch_data(cursor, row):
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]

    return data

# def base64_to_text(text):
#     decoded = base64.b64decode(text).decode('utf-8')
#     return decoded

dir_path = os.path.dirname(os.path.realpath(__file__)) 
database = dir_path + '/Questions.db'
conn = create_connection(database)

conn.row_factory = fetch_data
cur = conn.cursor()

cur.execute('select * from questions;')
dataList = cur.fetchall()
questions = []
for i in range(len(dataList)):
    data=dataList[i].get('question')
    questions.append(data)
    

# data = dataList[0].get('question')
# for i in range(len(questions)):
#     print(base64_to_text(questions[i][2:-1]) + "<br><br><br>")

for i in range(len(questions)):
    print(questions[i])