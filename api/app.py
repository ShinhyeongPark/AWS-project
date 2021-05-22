#Flask로 API 서버 만들기
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flaskext.mysql import MySQL
from datetime import datetime
import json
import pymysql

app = Flask(__name__)
api = Api(app) #Flask 객체에 Api 객체 등록

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    #DB password
    'password': '',
    #DB Name
    'database': ''
}


class SearchUser(Resource):
    def get(self, email):
        return {
            'user_mail': email
        }

class InsertUser(Resource):
    def __init__(self):
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('password', type=str)
            parser.add_argument('name', type=str)

            args = parser.parse_args()
            _userEmail = args['email']
            _userPassword = args['password']
            _userName = args['name']

            return {'Email': args['email'], 'Name': args['name'], 'Password': args['password']}
            
        except Exception as e:
            return {'error': str(e)}

api.add_resource(InsertUser, '/users/insert')

if __name__ == '__main__':
    app.run(port=8001, debug=True)