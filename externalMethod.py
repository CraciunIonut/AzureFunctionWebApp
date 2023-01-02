from flask import request, jsonify, Blueprint, render_template
import json
import requests

blueprintExternal = Blueprint('getExternalMethod', __name__)

@blueprintExternal.route('/', methods=['POST','GET'])
def query_record():
    if request.method == 'GET':
        return render_template("external.html")
    
    url = "http://openlibrary.org/search.json?author=" + request.form['author']

    response = requests.request("GET",url)
    json_response = json.loads(response.text)
    list_of_books = []

    for book in json_response['docs']:
        list_of_books.append(book['seed'][0])

    list_of_dict = []

    for i in range(10):
        if list_of_books[i].startswith("/books"):
            url = "http://openlibrary.org" + list_of_books[i] + ".json"
            response = requests.request("GET",url)
            json_response = json.loads(response.text)
            if str(json_response.get('publishers')) != "None" and str(json_response.get('number_of_pages')) != "None":
                dict = {'publishers' : json_response['publishers'], 'number_of_pages' : json_response['number_of_pages'], 'title' : json_response['title'] }
                list_of_dict.append(dict)

    return jsonify(list_of_dict)       