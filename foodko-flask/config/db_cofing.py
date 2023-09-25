

class DbConfig:
    HOSTNAME = '123.57.249.44'
    PORT = '3306'
    DATABASE = 'flasktest'
    USERNAME = 'flask'
    PASSWORD = '687939g'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
