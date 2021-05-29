#Public IP: 13.48.157.80
#EC2 Name : APIserver3

import os
import json
import time
import boto3
import socket
import requests
import datetime
from PIL import Image
from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_restful import Resource, reqparse, Api

app = Flask (__name__)

#[POST] http://[PublicIP]/arn:[PORT]
@app.route('/images', methods = ['POST'])
def imageDownload(): #전송된 이미지를 모델에 돌리고 결과를 저장
    image = request.files['image'] #이미지 수신
    imageName = secure_filename(image.filename) #이미지의 이름 저장
    image.save('/home/ubuntu/content/yolov5/results/'+imageName) #지정된 경로에 이미지 저장

    #AI 동작
    os.system('python3 detect.py --weights /home/ubuntu/content/best_disease_92.pt --img 416 --conf 0.7 --source /home/ubuntu/content/yolov5/results/'+imageName+' --save-txt --nosave')
    #AI 결과 -> 라벨링된 이미지를 S3에 저장
    s3 = boto3.client('s3',
                        aws_access_key_id = "",
                        aws_secret_access_key = "",
                        region_name = ""
                        )
    s3.upload_file('/home/ubuntu/content/yolov5/results/'+imageName, 'yangjae-team10-result', imageName)

    return "AI Success"


if __name__ == "__main__":
    app.run(host='172.31.205.193',port=8080, debug=True)