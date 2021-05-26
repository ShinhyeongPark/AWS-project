#Main Page
from flask import Flask, request, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

#http://127.0.0.1:8000/
@app.route('/')
def home(): #메인페이지 이동
    return render_template('index.html')

#http://127.0.0.1:8000/admin
@app.route('/admin') #관리자페이지 이동
def admin():
    return 'Admin Page'

if __name__ == '__main__':
    app.run(port=8000, debug=True)