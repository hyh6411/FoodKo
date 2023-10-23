from .init_sqlalchemy import db
from datetime import datetime
from sqlalchemy import Column, INTEGER, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ElementList(db.Model, Base):
    __tablename__ = 'Element_list'
    __table_args__ = {'comment': '营养元素表'}

    id = Column(String(50), primary_key=True)
    name = Column(String(50), server_default=text("'没有名字'"))
    chemical_tag = Column(String(50), server_default=text("''"))
    main_text = Column(String(2000), server_default=text("''"))
    alias = Column(String(50), server_default=text("''"), comment='别名')
    image = Column(String(255), server_default=text("''"))
    link = Column(String(255), server_default=text("''"), comment='链接，备用')
    icon = Column(String(50), server_default=text("''"))
    origin_food = Column(String(255), server_default=text("''"), comment='摄入来源，[id]的格式')
    origin_select = Column(String(255), server_default=text("''"), comment='摄入选择，文本')
    compute = Column(String(255), server_default=text("''"), comment="含量计算，{text: '', item: []}")
    heat = Column(INTEGER)
    back_color = Column(String(50), server_default=text("'blue'"))

    def to_dict(self):
        # 字典推导式
        data = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data

    def keys(self):
        return self.fields

