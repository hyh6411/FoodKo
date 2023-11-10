from .init_sqlalchemy import db
from datetime import datetime
from sqlalchemy import Column, INTEGER, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class IngredientsList(db.Model, Base):
    __tablename__ = 'ingredients_list'
    __table_args__ = {'comment': '食品原材料，比如土豆、西红柿、五花肉、羊肉、牛奶、大豆。。。'}

    id = Column(String(50), primary_key=True)
    name = Column(String(50), server_default=text("'还没有名字'"))
    nutrition_list = Column(String(2000), server_default=text("'[]'"), comment='储存元素的id和含量(g)，调查询后台查出来')
    cook_list = Column(String(2000), server_default=text("'[]'"))
    alias = Column(String(250), server_default=text("''"))
    main_text = Column(String(2000), server_default=text("'描述文本'"))
    icon = Column(String(200), server_default=text("''"))
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
