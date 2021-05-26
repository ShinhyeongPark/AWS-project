from flask import Flask, request, render_template
from flask_restful import Resource, reqparse, Api
from sqlalchemy import create_engine, text
from sqlalchemy.sql.functions import user
from flaskext.mysql import MySQL

#Flask <-> MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#로그인
class Signin(Resource):
    #http://127.0.0.1/signin
    @app.route('/signin')
    def signinPage():
        return render_template('signin.html')
    
    #[POST] http://127.0.0.1/signin
    @app.route('/signin', methods = ['POST'])
    def signinPost():
        email = request.form['user_email']
        password = request.form['user_password']

        conn = mysql.connect()
        cursor = conn.cursor()

        #입력데이터와 조회한 데이터를 비교
        sql = "SELECT user_password FROM users WHERE user_email = '%s'" % (email)
        cursor.execute(sql)

        data = cursor.fetchall()

        for d in data:
            print(d)

#회원가입
class Signup(Resource):
    #http://127.0.0.1/signup
    @app.route('/signup')
    def signupPage():
        return render_template('signup.html')

    #[POST] #http://127.0.0.1/signup
    @app.route('/signup', methods = ['POST'])
    def signupPost():
        email = request.form['user_email']
        password = request.form['user_password']
        name = request.form['user_name']

        conn = mysql.connect()
        cursor = conn.cursor()

        #데이터베이스에 사용자 정보 사입
        sql = "INSERT INTO users(user_email, user_password, user_name) VALUES ('%s', '%s', '%s')" % (email, password, name)
        cursor.execute(sql)

        data = cursor.fetchall()

        #회원가입 성공
        if not data:
            conn.commit()
            return render_template('signin.html')
        else: #실패
            conn.rollback()
            return "Register Failed"

        cursor.close()
        conn.close()
        return render_template('signup.html', error=error)
        

if __name__ == '__main__':
    app.run(port=8002, debug=True)