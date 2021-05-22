# 작물 및 병충해 분류/인식 서비스
> 융합프로젝트 [IoT + Bigdata + AI + Cloud]  

##  💡역할
```
1. JWT를 사용한 로그인/회원가입 페이지 구현
2. FLASK + API서버를 사용한 웹서비스 구현
3. 각 모듈(IoT, Bigdata, AI) 사이에 데이터 통신 구현
	- FLASK API Server
	- EC2에서 모듈 동작
	- S3에 객체(이미지) 생성시 람다 호출
	- 람다로 API에 JSON 데이터 POST
```

## 시스템 아키텍처
![중간](https://user-images.githubusercontent.com/57867611/119221992-17abf580-bb2d-11eb-801b-055c2b3d1f05.png)