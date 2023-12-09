from datetime import datetime
from flask import request, jsonify
import uuid
from flask import Blueprint
from flask_restful import Api, Resource
from models.init_sqlalchemy import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import RecordList, User
from ulit.result import ReBase


record_bp = Blueprint('record', __name__, url_prefix='/record/')


class QueryAllRecord(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        # 获取当前用户的记录
        user_name = get_jwt_identity()
        user = User.query.filter_by(user_name=user_name).first()
        record_list = RecordList.query.filter_by(use_id=user.id).all()
        # 将数据转换为数组
        record_array = []
        for record in record_list:
            record_array.append(record.to_dict())

        # 使用 jsonify 函数将数据转换为 JSON 格式并传递给前端
        return ReBase('1', obj=record_array).print()


class GetRecordById(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        id = request.args.get('id')
        if id:
            record = RecordList.query.filter_by(id=id).first()
            return ReBase('1', obj=record.to_dict()).print()
        else:
            return ReBase('2').print()


class GetRecordByDay(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        day_time = request.args.get('day_time')
        if day_time:
            user_name = get_jwt_identity()
            user = User.query.filter_by(user_name=user_name).first()
            record = RecordList.query.filter_by(day_time=day_time, use_id=user.id).first()
            return ReBase('1', obj=record.to_dict()).print()
        else:
            return ReBase('2').print()


class GetRecordByToDay(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        user_name = get_jwt_identity()
        user = User.query.filter_by(user_name=user_name).first()
        day_time = datetime.now().date()
        record = RecordList.query.filter_by(day_time=day_time, use_id=user.id).first()
        if record:
            return ReBase('1', obj=record.to_dict()).print()
        else:
            return ReBase('2', msg='今天还没有记录！').print()


class AddRecord(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # 生成id uuid1=根据MAC地址和时间戳生成
        id = str(uuid.uuid1())
        user_name = get_jwt_identity()
        user = User.query.filter_by(user_name=user_name).first()
        # 生成时间 如果重复就报错
        day_time = datetime.now().date()
        if RecordList.query.filter_by(day_time=day_time, use_id=user.id).first():
            return ReBase('2', msg="同一天只能有一条记录！").print()

        record = RecordList(id=id, day_time=day_time, use_id=user.id)
        for column in RecordList.__table__.columns:
            if column.name != 'day_time' and column.name in data:
                setattr(record, column.name, data[column.name])

        db.session.add(record)
        db.session.commit()
        return ReBase('1', obj=record.to_dict()).print()


class DeleteRecord(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        ids = data['ids']
        record = RecordList.query.filter(RecordList.id.in_(ids)).all()
        for r in record:
            db.session.delete(r)
        db.session.commit()
        return ReBase('1', '删除成功!').print()


class UpdateRecord(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        id = data['id']
        record = RecordList.query.filter_by(id=id).first()
        for column in RecordList.__table__.columns:
            if column.name in data:
                setattr(record, column.name, data[column.name])
        db.session.commit()
        return ReBase('1', obj=record.to_dict()).print()


class UpdateRecordByDateTime(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        day_time = datetime.now().date()
        user_name = get_jwt_identity()
        user = User.query.filter_by(user_name=user_name).first()
        record = RecordList.query.filter_by(day_time=day_time, use_id=user.id).first()
        if record:
            for column in RecordList.__table__.columns:
                if column.name != 'day_time' and column.name != 'id' and column.name in data:
                    setattr(record, column.name, data[column.name])
        else:
            # 没有就创建一条记录
            id = str(uuid.uuid1())
            record = RecordList(day_time=day_time, id=id, use_id=user.id)
            for column in RecordList.__table__.columns:
                if column.name != 'day_time' and column.name != 'id' and column.name in data:
                    setattr(record, column.name, data[column.name])
            db.session.add(record)

        db.session.commit()
        return ReBase('1', obj=record.to_dict()).print()


class AddQuestionNumber(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # number没传就取1
        number = data['number'] if 'number' in data else 1
        day_time = datetime.now().date()
        user_name = get_jwt_identity()
        user = User.query.filter_by(user_name=user_name).first()
        record = RecordList.query.filter_by(day_time=day_time, use_id=user.id).first()
        if record:
            # record.question_number 是 NONE
            if record.question_number is None:
                question_number = number
            else:
                question_number = record.question_number + number
            setattr(record, 'question_number', question_number)
        else:
            # 没有就创建一条记录
            id = str(uuid.uuid1())
            record = RecordList(day_time=day_time, id=id, use_id=user.id)
            question_number = number
            setattr(record, 'question_number', question_number)
            db.session.add(record)

        db.session.commit()
        return ReBase('1', obj=record.to_dict()).print()


api = Api(record_bp)
api.add_resource(QueryAllRecord, '/queryAll')
api.add_resource(GetRecordById, '/queryById')
api.add_resource(GetRecordByDay, '/queryByDay')
api.add_resource(GetRecordByToDay, '/queryByToDay')
api.add_resource(AddRecord, '/add')
api.add_resource(DeleteRecord, '/delete')
api.add_resource(UpdateRecord, '/update')
api.add_resource(UpdateRecordByDateTime, '/updateByDateTime')
api.add_resource(AddQuestionNumber, '/addQuestionNumber')
