from flask import Flask
from models.init_sqlalchemy import init_databases
from models.init_sqlalchemy import db
from api import _init_blueprint
from flask_migrate import Migrate
import config
from flask_jwt_extended import JWTManager
import models

app = Flask(__name__)


# 加载配置
app.config.from_object(config.DevelopmentConfig)

# jwt初始化
jwt = JWTManager(app)

# 重写sqlalchemy
init_databases(app)

# 初始化数据库
# db.init_app(app)

migrate = Migrate(app, db)

_init_blueprint(app)


if __name__ == '__main__':
    app.run(debug=True, host='172.24.93.207')