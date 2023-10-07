import json

from flask import request
from flask import Blueprint
from flask_restful import Api, Resource
from models.init_sqlalchemy import db
from models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
from ulit.result import ReBase


bp = Blueprint('account', __name__, url_prefix='/account/')

blacklist = set()


def check_if_token_in_blacklist():
    token = get_jwt()
    jti = token['jti']
    return jti in blacklist  # 检查token是否在黑名单中


class Login(Resource):

    def post(self):
        data = request.get_json()
        name = data['name']
        pass_ = data['pass']
        print('name=' + name + ' pass=' + pass_)
        user = User.query.filter_by(user_name=name).first()
        if user:
            print('pass: ' + user.password_hash)
            if user.validate_password(password=pass_):
                # 身份验证逻辑，验证成功后生成访问令牌和刷新令牌
                access_token = create_access_token(identity=user.user_name)
                refresh_token = create_refresh_token(identity=user.user_name)
                return ReBase('1', '登录成功!', {'access_token': access_token, 'refresh_token': refresh_token, 'user_name': user.user_name}).print()
            else:
                return ReBase('2', '密码错误!', {
                    'user_name': user.user_name
                }).print()
            pass
        else:
            return ReBase('2', '查无此人!').print()


class Logout(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        # 获取当前用户身份标识
        token = get_jwt()
        blacklist.add(token['jti'])
        return ReBase('1', '退出成功!').print()


class Refresh(Resource):
    method_decorators = [jwt_required(refresh=True)]  # 使用刷新令牌进行身份验证

    def get(self):
        if check_if_token_in_blacklist():
            return ReBase('2', '登录失败!').print()
        # 获取当前用户身份标识
        current_user = get_jwt_identity()
        # 刷新访问令牌
        new_access_token = create_access_token(identity=current_user)
        return ReBase('1', '刷新成功!', {'access_token': new_access_token}).print()


class AddUser(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        name = data['name']
        password = data['pass']
        user = User(user_name=name, pass_word=password)
        # user对象会自动加密密码
        db.session.add(user)
        db.session.commit()
        return ReBase('1', '注册成功!').print()


class DeleteUser(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        user_id = data['id']
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return ReBase('1', '删除成功!').print()


class UpdateUser(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        # 修改用户信息
        data = request.get_json()
        user_id = data['id']
        user_data = data['user']
        user = User.query.filter_by(id=user_id).first()
        # 遍历user，获取需要修改的字段并修改
        for key, value in user_data.items():
            if key == 'id':
                continue
            setattr(user, key, value)
        db.session.commit()
        return ReBase('1', '修改成功!').print()


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
            return ReBase('1', obj=user.to_dict()).print()


api = Api(bp)
api.add_resource(Login, '/login/', endpoint='login')
api.add_resource(Refresh, '/refresh/', endpoint='refresh')
api.add_resource(AddUser, '/add/', endpoint='add')
api.add_resource(DeleteUser, '/delete/', endpoint='delete')
api.add_resource(UpdateUser, '/update/', endpoint='update')
api.add_resource(UserInfo, '/queryUserInfo/', endpoint='userInfo')
