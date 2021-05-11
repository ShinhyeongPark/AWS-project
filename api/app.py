#Flask로 API 서버 만들기
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app) #Flask 객체에 Api 객체 등록

#예시로 todos에 저장 -> 이제는 DB에 저장
todos = {}
count = 1

@api.route('/todos') #Body에 데이터 전송
class TodoPost(Resource):
    #회원가입
    def post(self):
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {
            'todo_id': idx,
            'data': todos[idx]
        }

@api.route('/todos/<int:todo_id>')
class TodoSimple(Resource):
    #로그인
    def get(self, todo_id):
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    #회원정보 수정
    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    #회원탈퇴
    def delete(self,todo_id):
        del todos[todo_id]
        return {
            "delete" : "succes"
        }


if __name__ == '__main__':
    app.run(port=8001)