
from .base_table import BaseTable
from .init_sqlalchemy import db
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, BaseTable):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment='用户id')
    user_name = db.Column(db.String(12), comment='用户名')
    pass_word = db.Column(db.String(12), comment='密码')
    sex = db.Column(TINYINT(1), comment='性别')
    weight = db.Column(TINYINT(5), comment='体重')
    password_hash = db.Column(db.String(150), comment='哈希密码')
    account = db.Column(db.String(10), comment='账号')
    introduce = db.Column(db.String(100), default='该用户还没有介绍！', comment='自我介绍')
    phone = db.Column(db.String(12), comment='手机号')
    vx = db.Column(db.String(20), comment='微信号')
    qq = db.Column(db.String(20), comment='QQ号')
    university = db.Column(db.String(20), comment='大学')
    specialty = db.Column(db.String(20), comment='专业')
    hobby = db.Column(db.String(50), comment='爱好')
    city = db.Column(db.String(10), default='南昌', comment='所在城市')

    @property
    def pass_word(self) -> None:
        pass

    @pass_word.setter
    def pass_word(self, pass_word):
        self.password_hash = generate_password_hash(pass_word)

    def validate_password(self, password):
        print('hash:' + self.password_hash + ',pass:' + password)
        return check_password_hash(self.password_hash, password)

    def to_str(self):
        return '(User: name: {}, pass_hash: {})'.format(self.user_name, self.password_hash)

    def to_dict(self):
        # 字典推导式，过滤掉密码
        data = {column.name: getattr(self, column.name) for column in self.__table__.columns if column.name != 'password_hash'}
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data

    def keys(self):
        return self.fields

    def __getitem__(self, item):
        return getattr(self, item)
