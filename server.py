from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

import psycopg2
import psycopg2.extras
import datetime as dt
from flask_cors import CORS

connection = psycopg2.connect(user = "postgres",
                              password = "chicken!1",
                              host = "localhost",
                              port = "5432",
                              database = "stockSimulator")
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

db_connect = create_engine('postgresql://postgres:chicken!1@localhost:5432/stockSimulator')
conn = db_connect.connect()
app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('fullname')
parser.add_argument('password')

class Users(Resource):
    def get(self):
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users)

# curl http://127.0.0.1:5003/users/ -d "username=test1" -d "fullname=test1" -d "password=test1" -v

    def post(self):
        args = parser.parse_args()
        cursor.execute("""
        INSERT INTO users (username, fullname, password)
        VALUES (%s, %s, %s);
        """, (args['username'], args['fullname'], args['password']))
        connection.commit()


api.add_resource(Users, '/users/')

if __name__ == '__main__':
    app.run(port='5003', debug=True)