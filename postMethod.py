from flask import request, Blueprint, render_template
import sqlite3

blueprintPost = Blueprint('postMethod', __name__)

@blueprintPost.route('/', methods=['POST', 'GET'])
def query_record():
    if request.method == "POST":
        connection = sqlite3.connect("db/users.db")
        cursor = connection.cursor()
        _id = request.form['id']
        _name = request.form['name']
        _password = request.form['password']

        query = "Insert into Users (id, name, password) VALUES({},'{}','{}')".format(int(_id),_name,_password)

        try:
            cursor.execute(query)
            connection.commit()
            verify = cursor.fetchone()
            if not verify:
                connection.close()
                return "Succesful sending data"
            
            else:
                connection.close()
                return "Failure sending data"
        
        except Exception as e:
            connection.close()
        
        return "Failure while sending data"

    return render_template("postform.html")

    