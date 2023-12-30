

class DbConfig:
    HOSTNAME = 'localhost'
    PORT = '3306'
    DATABASE = 'foodko'
    USERNAME = 'root'
    PASSWORD = '687939g'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
