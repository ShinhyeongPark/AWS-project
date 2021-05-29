#Socket 통신 서버
#Public IP: 13.48.157.80
##EC2 Name : APIserver3
import os
import json
import time
import boto3
import socket
import requests
import datetime
from PIL import Image
from flask import Flask, request
from flask_restful import Resource, reqparse, Api

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#소켓통신 재연결시 동시한 IP를 사용 가능하도록 하는 설정
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server_socket.bind(('ec2-13-48-157-80.eu-north-1.compute.amazonaws.com', 9999))
server_socket.listen() #클라이언트 접속 대기
client_socket, addr = server_socket.accept() #클라이언트 연결 성공

#계속 통신
while True:
    #클라이언트로 부터 이미지의 이름 수신
    time.sleep(2) #요청은 왔으나, 이미지에 대한 결과가 도출되는데 2~3초 정도 걸리므로 Sleep
    #대기 후, 요청받은 이미지의 이름에 대한 결과를 조회 후 클라이언트로 전송 
    client_socket.send("1.0".encode("utf-8"))

#통신 종료
client_socket.close()
server_socket.close()

