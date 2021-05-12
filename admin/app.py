#Main Page
from flask import Flask, request, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.config.from_pyfile('../config.py')
#[MySQL DB연동]
database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
app.database = database

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return 'Admin Page'

if __name__ == '__main__':
    app.run(port=8000, debug=True)