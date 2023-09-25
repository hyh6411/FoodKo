import datetime
from .init_sqlalchemy import db


class BaseTable:
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
    delete_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='删除时间')
