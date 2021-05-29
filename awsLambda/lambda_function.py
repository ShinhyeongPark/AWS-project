import json
import boto3
import pymysql
import requests
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    #DB 접속
    conn = pymysql.connect(
        host = '', #Public IP
        user = 'root', #user name
        password = '', #DB password
        db = '', #DB name
        charset = 'utf8',
        port = 3309 #PORT
    )
    
    curs = conn.cursor()
    #DB에 ARN 저장
    sql = 'INSERT INTO arn (arn) VALUES (%s)'
    curs.execute(sql,(event['Records'][0]['s3']['bucket']['arn']+'/'+event['Records'][0]['s3']['object']['key']))
    conn.commit()
    
    url = 'http://13.48.96.136:8088/arn'
    arn = event['Records'][0]['s3']['bucket']['arn']+'/'+event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_path = event['Records'][0]['s3']['object']['key']
    
    datas = {}
    datas['arn'] = arn
    datas['bucket_name'] = bucket_name
    datas['file_path'] = file_path
    json_data = json.dumps(datas)
    
    reponse = requests.post(url, data=json_data)
    return 
