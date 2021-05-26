import json
import boto3
from flask import Flask, request
from flask_restful import Resource, reqparse, Api

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#[POST] http://[PublicIP]/arn:[PORT]
@app.route('/result', methods = ['POST'])
def imageDownload():
    #json으로 전송한 데이터를 저장
    data = json.loads(request.get_data(), encoding='utf-8')

    arn = data['arn'] #arn을 비교 후 결과에 따라 액션을 취한 뒤 DB에 해당 ARN 삭제
    result = data['result']
    acc = data['acc']

    return data


if __name__ == "__main__":
    app.run(host='[PrivateKey]',port=8080, debug=True)