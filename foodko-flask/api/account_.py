from flask import request
from flask import Blueprint
from flask_restful import Api, Resource
from models.init_sqlalchemy import db
from models.user import User
from flask_jwt_extended import create_access_token, jwt_required
from ulit.result import ReBase


bp = Blueprint('account', __name__, url_prefix='/account/')


class Login(Resource):

    def post(self):
        name = request.form.get('name')
        pass_ = request.form.get('pass')
        print('name=' + name + ' pass=' + pass_)
        user = User.query.filter_by(user_name=name).first()
        if user:
            print('pass: ' + user.password_hash)
            if user.validate_password(password=pass_):
                access_token = create_access_token(identity=user.user_name)
                return ReBase('1', '登录成功!', {'access_token': access_token}).print()
            else:
                return ReBase('2', '密码错误!', {
                    'user_name': user.user_name
                }).print()
            pass
        else:
            return ReBase('2', '查无此人!').print()


class AddUser(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        name = request.form.get('name')
        password = request.form.get('pass')
        user = User(user_name=name, pass_word=password)
        # user对象会自动加密密码
        db.session.add(user)
        db.session.commit()
        return ReBase('1', '注册成功!')


class UserInfo(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        name = request.args.get('name')
        id = request.args.get('id')
        if name:
            user = User.query.filter_by(user_name=name).first()
        elif id:
            user = User.query.filter_by(id=id).first()
        else:
            return ReBase('2')
        if user:
            return ReBase('1', obj={
                'user': dict(user)
            })


api = Api(bp)
api.add_resource(Login, '/login/', endpoint='login')
api.add_resource(AddUser, '/add/', endpoint='add')
api.add_resource(UserInfo, '/queryUserInfo/', endpoint='userInfo')
