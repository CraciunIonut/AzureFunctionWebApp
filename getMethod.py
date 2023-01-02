from flask import request, jsonify, Blueprint, render_template
import sqlite3

blueprintGet = Blueprint('getMethod', __name__)

@blueprintGet.route('/', methods=['POST','GET'])
def query_record():
    if request.method == "GET":
        return render_template("getform.html")
    
    else:
        _id = request.form['id']
        connection = sqlite3.connect("db/users.db")
        cursor = connection.cursor()

        query_verify = "Select exists(Select name from Users where id = {})".format(_id)
        result_verify = cursor.execute(query_verify)

        if str(result_verify.fetchall()[0][0]) == "1":
             query = "Select name from Users where id = {}".format(_id)
             result = cursor.execute(query)
             result = result.fetchall()[0][0]
             return "Name is : " + result
        
        else:
             return "Invalid index"
    