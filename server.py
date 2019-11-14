from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

import psycopg2
import datetime as dt
from flask_cors import CORS

connection = psycopg2.connect(user = "postgres",
                              password = "chicken!1",
                              host = "localhost",
                              port = "5432",
                              database = "stockSimulator")
cursor = connection.cursor()

db_connect = create_engine('postgresql://postgres:chicken!1@localhost:5432/stockSimulator')
conn = db_connect.connect()
app = Flask(__name__)
CORS(app)
api = Api(app)

class Users(Resource):
    def get(self, date):
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return {users}

api.add_resource(Users, '/users/')

if __name__ == '__main__':
    app.run(port='5002')