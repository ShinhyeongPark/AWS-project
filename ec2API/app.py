#EC2 FLASK API
#EC2 Name: APIserver
#PUPLIC IP: 13.48.96.136

import os
import json
import boto3
import requests
from flask import Flask, request
from flask_restful import Resource, reqparse, Api

app = Flask (__name__)

#S3 객체에 정보를 이용해 이미지 저장
def downloadFromS3(strBucket, s3_path, local_path):
    s3_client = boto3.client(
        's3',
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name = ""
    )
    s3_client.download_file(strBucket, s3_path, local_path)

#[POST] http://PublicIP:[PORT]/arn
@app.route('/arn', methods = ['POST'])
def imageDownload():
    #POST 데이터를 저장 (객체에 대한 Data)
    tmp = json.loads(request.get_data(), encoding='utf-8')
    
    #[객체 정보]
    arn = tmp['arn']
    bucket_name = tmp['bucket_name']
    file_path = tmp['file_path']
    file_name = file_path.split('/')[-1]

    downloadFromS3(bucket_name, file_path, '/tmp/'+file_name)

    url = 'http://13.48.157.80:8080/images'
    img = open('/tmp/'+file_name, 'rb')
    files = {'image' : img}
    #S3에 접근해 객체 이미지 저장 후 전송
    r = requests.post(url, files=files)
    img.close()
    
    return "ARN Send Success"

if __name__ == "__main__":
    app.run(host='172.31.0.147',port=8088, debug=True)