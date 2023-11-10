from flask import request, jsonify
import uuid
from flask import Blueprint
from flask_restful import Api, Resource
from models.init_sqlalchemy import db
from flask_jwt_extended import jwt_required, get_jwt
from models import QuestionList
from ulit.result import ReBase


question_bp = Blueprint('question', __name__, url_prefix='/question/')


class QueryQuestion(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        # 获取题库
        question_list = QuestionList.query.all()
        # 将数据转换为数组
        question_array = []
        for question in question_list:
            question_array.append(question.to_dict())

        # 使用 jsonify 函数将数据转换为 JSON 格式并传递给前端
        return ReBase('1', obj=question_array).print()
        pass


class GetQuestion(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        id = request.args.get('id')
        number = request.args.get('number')
        if id:
            question = QuestionList.query.filter_by(id=id).first()
            return ReBase('1', obj=question.to_dict()).print()
        elif number:
            # 随机抽取题目
            # 获取表中的总条数
            question_list = QuestionList.get_random_question(self=QuestionList, n=int(number))
            question_list = [question.to_dict() for question in question_list]
            return ReBase('1', obj=question_list).print()
        pass


class AddQuestion(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # 生成id uuid1=根据MAC地址和时间戳生成
        id = str(uuid.uuid1())
        content = data['content']
        option = data['option']
        remark = data['remark']
        explain = data['explain']
        answer = data['answer']
        question = QuestionList(id=id, content=content, option=option, remark=remark, explain=explain, answer=answer)
        db.session.add(question)
        db.session.commit()
        return ReBase('1', '添加成功!', obj=question.to_dict()).print()


class DeleteQuestion(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        ids = data['ids']
        question = QuestionList.query.filter(QuestionList.id.in_(ids)).all()
        for q in question:
            db.session.delete(q)
        db.session.commit()
        return ReBase('1', '删除成功!').print()


class UpdateQuestion(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        id = data['id']
        content = data['content']
        option = data['option']
        remark = data['remark']
        explain = data['explain']
        answer = data['answer']
        question = QuestionList.query.filter_by(id=id).first()
        question.content = content
        question.option = option
        question.remark = remark
        question.explain = explain
        question.answer = answer
        db.session.commit()
        return ReBase('1', '修改成功!').print()


api = Api(question_bp)
api.add_resource(QueryQuestion, '/queryAllQuestion/', endpoint='queryAllQuestion')
api.add_resource(GetQuestion, '/getQuestion/', endpoint='getQuestion')
api.add_resource(AddQuestion, '/addQuestion/', endpoint='addQuestion')
api.add_resource(DeleteQuestion, '/deleteQuestion/', endpoint='deleteQuestion')
api.add_resource(UpdateQuestion, '/updateQuestion/', endpoint='updateQuestion')

