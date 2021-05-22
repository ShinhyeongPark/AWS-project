import json
import boto3
from flask import Flask, request
from flask_restful import Resource, reqparse, Api

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#S3에 있는 이미지 저장
def downloadFromS3(strBucket, s3_path, local_path):
    s3_client = boto3.client(
        's3',
        aws_access_key_id="Access-Key",
        aws_secret_access_key="Secre-access-Key",
        region_name = "Region"
    )
    s3_client.download_file(strBucket, s3_path, local_path)

#[POST] http://[PublicIP]/arn:[PORT]
@app.route('/arn', methods = ['POST'])
def imageDownload():
    #json으로 전송한 데이터를 저장
    data = json.loads(request.get_data(), encoding='utf-8')

    arn = data['arn']
    bucket_name = data['bucket_name']
    file_path = data['file_path']
    file_name = file_path.split('/')[-1]

    #이미지 다운로드 [저장위치: tmp디렉터리]
    downloadFromS3(bucket_name, file_path, '/tmp/'+file_name)
    return data


if __name__ == "__main__":
    app.run(host='PrivateIP',port=8080, debug=True)