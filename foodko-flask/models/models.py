# coding: utf-8
from sqlalchemy import Column, Date, DateTime, ForeignKey, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ElementList(Base):
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
    heat = Column(INTEGER(11))
    back_color = Column(String(50), server_default=text("'blue'"), comment='背景颜色')


class FoodList(Base):
    __tablename__ = 'food_list'
    __table_args__ = {'comment': '食谱、美食区'}

    id = Column(String(50), primary_key=True, server_default=text("''"))
    name = Column(String(50), server_default=text("'还没有名字'"))
    alias = Column(String(50), server_default=text("''"))
    ingredients = Column(String(2000), server_default=text("''"))
    tag = Column(String(200), server_default=text("''"), comment='菜的类型：面食、主食。。。')
    local = Column(String(50), server_default=text("''"), comment='发源地')
    hat = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='热量')
    main_text = Column(Text)
    production_method = Column(Text)
    production_type = Column(String(50), server_default=text("''"), comment='制作类型：蒸煮烤。。')
    image = Column(String(200), server_default=text("''"))


class IngredientsList(Base):
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


class QuestionList(Base):
    __tablename__ = 'question_list'
    __table_args__ = {'comment': '题库'}

    id = Column(String(50), primary_key=True)
    content = Column(String(255), server_default=text("'空问题'"))
    option = Column(String(255), server_default=text("'空选项'"))
    remark = Column(String(255), server_default=text("''"))
    explain = Column(String(255), server_default=text("'因为所以，科学道理'"))
    answer = Column(String(2), server_default=text("'a'"))


class Test(Base):
    __tablename__ = 'test'

    create_time = Column(DateTime, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')
    delete_time = Column(DateTime, comment='删除时间')
    id = Column(INTEGER(11), primary_key=True, comment='用户id')
    name = Column(INTEGER(11), comment='test')


class User(Base):
    __tablename__ = 'user'

    create_time = Column(DateTime, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')
    delete_time = Column(DateTime, comment='删除时间')
    id = Column(INTEGER(11), primary_key=True, comment='用户id')
    user_name = Column(String(12), comment='用户名')
    account = Column(String(10), comment='账号')
    introduce = Column(String(100), comment='自我介绍')
    phone = Column(String(12), comment='手机号')
    vx = Column(String(20), comment='微信号')
    qq = Column(String(20), comment='QQ号')
    university = Column(String(20), comment='大学')
    specialty = Column(String(20), comment='专业')
    hobby = Column(String(50), comment='爱好')
    city = Column(String(10), comment='所在城市')
    password_hash = Column(String(150), comment='哈希密码')
    sex = Column(TINYINT(1), comment='性别')
    weight = Column(TINYINT(5), comment='体重(kg)')


class Recored(Base):
    __tablename__ = 'recored'
    __table_args__ = {'comment': '用户每日活动记录'}

    id = Column(String(50), primary_key=True)
    question_number = Column(INTEGER(11))
    eat_list = Column(Text)
    jrink = Column(String(50))
    read_record = Column(Text)
    day_time = Column(Date, nullable=False)
    use_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    use = relationship('User')
