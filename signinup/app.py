from flask import Flask, request, render_template
from flask_restful import Resource, reqparse, Api
from sqlalchemy import create_engine, text
from sqlalchemy.sql.functions import user
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#로그인
class Signin(Resource):
    @app.route('/signin')
    def signinPage():
        return render_template('signin.html')
    
    @app.route('/signin', methods = ['POST'])
    def signinPost():
        email = request.form['user_email']
        password = request.form['user_password']

        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "SELECT user_password FROM users WHERE user_email = '%s'" % (email)
        cursor.execute(sql)

        data = cursor.fetchall()

        for d in data:
            print(d)
        # if data == password:
        #     print('succes')
        # else:
        #     print('flase')


class Signup(Resource):
    @app.route('/signup')
    def signupPage():
        return render_template('signup.html')

    @app.route('/signup', methods = ['POST'])
    def signupPost():
        email = request.form['user_email']
        password = request.form['user_password']
        name = request.form['user_name']

        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "INSERT INTO users(user_email, user_password, user_name) VALUES ('%s', '%s', '%s')" % (email, password, name)
        cursor.execute(sql)

        data = cursor.fetchall()

        if not data:
            conn.commit()
            return render_template('signin.html')
        else:
            conn.rollback()
            return "Register Failed"

        cursor.close()
        conn.close()
        return render_template('signup.html', error=error)
        

if __name__ == '__main__':
    app.run(port=8002, debug=True)