#Flask & Database 연동

db = {
    'user'     : 'root',
    'password' : 'mysql',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'users'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 