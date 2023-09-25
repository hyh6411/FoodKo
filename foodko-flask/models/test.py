from .base_table import BaseTable
from .init_sqlalchemy import db


class Test(BaseTable, db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, comment='用户id')
    name = db.Column(db.Integer, comment='test')
    pass
