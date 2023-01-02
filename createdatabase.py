import sqlite3

def createdb():
    connection = sqlite3.connect('db/users.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
    (id integer primary key autoincrement, name text, password text)''')
    connection.close()