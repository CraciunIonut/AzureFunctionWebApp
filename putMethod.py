from flask import request, Blueprint, render_template
import sqlite3

blueprintPut = Blueprint('putMethod', __name__)

@blueprintPut.route('/', methods=['POST', 'PUT', 'GET'])
def query_record():
    if request.method == "POST" or request.method == "PUT":    
        connection = sqlite3.connect("db/users.db")
        cursor = connection.cursor()
        _id = request.form['id']
        _name = request.form['name']

        query = "Update Users set name = '{}' where id = {}".format(_name,int(_id))

        cursor.execute(query)
        connection.commit()
        connection.close()

        return "Succesful"
    return render_template("putform.html")