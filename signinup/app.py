from flask import Flask, request, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.config.from_pyfile('config.py')
#[MySQL DB연동]
database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
app.database = database
# app.config["DEBUG"] = True
#로그인
@app.route('/signin')
def signin():
    return render_template('signin.html')

#회원가입
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(port=8002)