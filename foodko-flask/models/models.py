# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


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
