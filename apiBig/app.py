from flask import Flask, request
from flask_restful import Resource, reqparse, Api
app = Flask (__name__)
import boto3

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/arn', methods = ['POST'])
def imageDownload():
    data = request.get_json()
    print(data)
    arn = data['arn']
    bucket_name = data['bucket_name']
    file_path = data['file_path']
    file_name = file_path.split('/')[-1]

    downloadFromS3(bucket_name, file_path, '/tmp/'+file_name)
    return arn


if __name__ == "__main__":
    app.run(host='private',port=9000, debug=True)