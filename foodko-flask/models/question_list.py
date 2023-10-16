from .init_sqlalchemy import db
from datetime import datetime
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.ext.declarative import declarative_base
from random import sample

Base = declarative_base()


class QuestionList(db.Model, Base):
    __tablename__ = 'question_list'
    __table_args__ = {'comment': '题库'}

    id = Column(String(50), primary_key=True)
    content = Column(String(255), server_default=text("'空问题'"))
    option = Column(String(255), server_default=text("'空选项'"))
    remark = Column(String(255), server_default=text("''"))
    explain = Column(String(255), server_default=text("'因为所以，科学道理'"))
    answer = Column(String(2), server_default=text("'a'"))

    def to_dict(self):
        # 字典推导式
        data = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data

    def keys(self):
        return self.fields

    # 随机抽取 n 条数据
    def get_random_question(self, n):
        # 查询所有数据
        all_question = self.query.all()

        # 随机抽取 n 条数据
        random_question = sample(all_question, n)

        return random_question

