from .init_sqlalchemy import db
from datetime import datetime
from sqlalchemy import Column, INTEGER, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FoodList(db.Model, Base):
    __tablename__ = 'food_list'
    __table_args__ = {'comment': '食谱、美食区'}

    id = Column(String(50), primary_key=True, server_default=text("''"))
    name = Column(String(50), server_default=text("'还没有名字'"))
    alias = Column(String(50), server_default=text("''"))
    ingredients = Column(String(2000), server_default=text("''"))
    tag = Column(String(50), server_default=text("''"), comment='菜的类型：面食、主食。。。')
    local = Column(String(50), server_default=text("''"), comment='发源地')
    hat = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='热量')
    main_text = Column(Text)
    production_method = Column(Text)
    production_type = Column(String(50), server_default=text("''"), comment='制作类型：蒸煮烤。。')
    image = Column(String(200), server_default=text("''"))

    def to_dict(self):
        # 字典推导式
        data = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data

    def keys(self):
        return self.fields
