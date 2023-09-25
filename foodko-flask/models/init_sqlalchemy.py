import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# query扩展方法
# class Query(BaseQuery):
#     # 软删除
#     def soft_delete(self):
#         return self.update({"delete_at": datetime.datetime.now()})
#
#     def logic_all(self):
#         return self.filter_by(delete_at=None).all()
# query_class=Query

db = SQLAlchemy()


def init_databases(app: Flask):
    db.init_app(app)
    # db.create_all()
