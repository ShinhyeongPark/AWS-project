# 작물 및 병충해 분류/인식 서비스
## 📌 Abstract
- 병충해와 잡초를 인식해 자동으로 분류하고 분석결과에 따라 약을 뿌리는 서비스
- IoT + Bigdata + AI + **Cloud** 기술을 사용한 융합 프로젝트

## ➡️ Flow
<img width="1587" alt="스크린샷 2021-06-07 오전 10 44 43" src="https://user-images.githubusercontent.com/57867611/120948603-8ae47700-c77d-11eb-9f16-201f65f54d4b.png">

## 💡 Role
1. 서비스 간 데이터 연결 구축
	- S3 이미지 추가시 Lambda 호출
	- S3 객체 ARN을 DB에 저장 및 API로 전송하는 Lambda 구현
	- S3 객체 데이터를 사용해 S3의 이미지를 로드하는 기능 구현
	- 이미지 수신시 자동으로 AI 동작 및 결과를 S3와 DB에 저장 기능 구현
	- IoT와 EC2간의 데이터 송수신을 위한 소켓 프로그래밍 구현
2. 서비스에 필요한 Database 운영을 위한 Docker-compose 작성
3. 서비스에 필요한 Web 구현
	- JWT를 사용한 로그인/회원가입 페이지
	- 메인 페이지

## ⚙️ System Architecture
![final](https://user-images.githubusercontent.com/57867611/120060580-8b04b880-c093-11eb-91ba-a5af17be0947.png)

1. IoT가 작물이미지를 촬영하면, 그 이미지를 S3에 저장하고 소켓통신을 통해 이미지의 이름을 서버로 전송
2. 람다의 트리거인 S3에 객체가 업로드되면, 객체의 ARN, 객체의 이름을 API로 전송하는 람다가 호출됩니다.(이미지를 전송하는게 아닌 이미지의 데이터를 전송)
3. API로 객체에 대한 데이터가 들어오면, 데이터를 이용해 S3 이미지를 저장한 후 AI모델이 있는 서버로 이미지를 전송한다.
4. 이미지를 받은 후 AI 모델링 결과(결과이미지, 정확도)를 각각 S3와 DB에 저장한다.
5. 또한 이전에 클라이언트로 부터 요청받은 이미지의 이름과 일치하는 모델링 결과를 클라이언트로 전송한다.
6. 모델링 결과를 수신한 IoT는 결과값에 따라 액션을 취한다.

## ✓ Tech Stack (Cloud)
<img width="566" alt="TechStack" src="https://user-images.githubusercontent.com/57867611/120060105-c356c780-c090-11eb-88c0-0e06a0d8f709.png">

## ✍︎ Issue
1. S3 이미지 업로드시 람다가 3번 호출되는 오류
	- 상황: S3에 이미지를 업로드 하면 람다를 자동 호출하도록 구현했는데, 람다를 1번이 아닌 3번 호출
	- 원인: 람다 함수에 문제로 판단이 되어 return이 실패했는지, 잘못된 값을 POST했는지를 분석했으나 정상적으로 리턴과 POST를 했다. 코드에 문제가 없다는 것을 확인하고 람다의 구성-> 비동기식 호출을 확인했을 때, 재시도 횟수가 2번으로 설정된 것을 확인
	- 해결: 우선 재시도가 일어난다는 것은 오류로 인해 발생하는 것이기 때문에 코드를 다시 한번 확인 후 데이터를 전송한 후 return이 없어 되돌아 오는 값이 들어오지 않다는 것을 확인할 수 있었고 이를 수정 
	추가적으로 비동기식 호출의 재시도 횟수를 0회로 변경

## 🔍 Classification
<img width="550" alt="스크린샷 2021-06-07 오전 10 45 11" src="https://user-images.githubusercontent.com/57867611/120948843-1100bd80-c77e-11eb-8873-29624d67bc54.png">

## 🌿 Service
<img width="500" alt="스크린샷 2021-06-07 오전 10 57 51" src="https://user-images.githubusercontent.com/57867611/120950338-87eb8580-c781-11eb-8baa-f3dd4205e62c.png">
<img width="500" alt="스크린샷 2021-06-07 오전 10 57 19" src="https://user-images.githubusercontent.com/57867611/120950357-9174ed80-c781-11eb-9006-0e59d0ef51ce.png">
