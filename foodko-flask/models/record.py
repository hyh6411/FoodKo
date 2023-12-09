
from .init_sqlalchemy import db
from datetime import datetime, date
from sqlalchemy import Column, Date, String, text, Text, INTEGER, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from random import sample

Base = declarative_base()


class RecordList(db.Model, Base):
    __tablename__ = 'recored'
    __table_args__ = {'comment': '用户每日活动记录'}

    id = Column(String(50), primary_key=True)
    question_number = Column(INTEGER, server_default=text("'0'"))
    eat_list = Column(Text)
    jrink = Column(String(50))
    read_record = Column(Text)
    day_time = Column(Date, nullable=False)
    use_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    use = relationship('User')

    def to_dict(self):
        # 字典推导式
        data = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        for key, value in data.items():
            if isinstance(value, (date, datetime)):
                data[key] = value.strftime('%Y-%m-%d')
        return data

    def keys(self):
        return self.fields
