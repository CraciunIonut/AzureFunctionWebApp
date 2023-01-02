from flask import Flask, jsonify, render_template
from flask_restful import Api

from getMethod import blueprintGet
from postMethod import blueprintPost
from mainMethod import blueprintMain
from externalMethod import blueprintExternal
from putMethod import blueprintPut

from createdatabase import createdb

app = Flask(__name__)
api = Api(app)

api_rest_host = "0.0.0.0"
api_rest_port = 5001

createdb()

app.register_blueprint(blueprintMain, url_prefix='/')
app.register_blueprint(blueprintGet, url_prefix='/Find')
app.register_blueprint(blueprintPost, url_prefix='/Register')
app.register_blueprint(blueprintExternal, url_prefix='/External')
app.register_blueprint(blueprintPut, url_prefix='/ChangeName')

app.run(host=api_rest_host, port=api_rest_port, debug=True)