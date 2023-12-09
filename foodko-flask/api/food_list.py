from flask import request, jsonify
import uuid
from flask import Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt
from models.init_sqlalchemy import db
from models import FoodList
from ulit.result import ReBase


food_dp = Blueprint('food', __name__, url_prefix='/food/')


class QueryAllFood(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        # 获取全部食谱
        food_list = FoodList.query.all()
        # 将数据转换为数组
        food_arr = []
        for food in food_list:
            food_arr.append(food.to_dict())

        # 使用 jsonify 函数将数据转换为 JSON 格式并传递给前端
        return ReBase('1', obj=food_arr).print()
        pass


class QueryFoodById(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        id = request.args.get('id')
        food_bp = FoodList.query.filter_by(id=id).first()

        return ReBase('1', obj=food_bp.to_dict()).print()


class AddFood(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # 生成id uuid1=根据MAC地址和时间戳生成
        id = str(uuid.uuid1())
        # 上面的简化写法
        food = FoodList(id=id)
        for column in FoodList.__table__.columns:
            if column.name in data:
                setattr(food, column.name, data[column.name])
        db.session.add(food)
        db.session.commit()
        # 使用 jsonify 函数将数据转换为 JSON 格式并传递给前端
        return ReBase('1', obj=food.to_dict()).print()


class DeleteFood(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        ids = data['ids']
        for id in ids:
            food = FoodList.query.filter_by(id=id).first()
            if food:
                db.session.delete(food)
        db.session.commit()
        return ReBase('1', '删除成功!').print()


class UpdateFood(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # 上面的简化写法
        food_id = data['id']
        food = FoodList.query.filter_by(id=food_id).first()
        for column in FoodList.__table__.columns:
            if column.name in data:
                setattr(food, column.name, data[column.name])

        db.session.commit()
        return ReBase('1', '修改成功!', obj=food.to_dict()).print()


api = Api(food_dp)
api.add_resource(QueryAllFood, '/queryAll/', endpoint='queryAllFood')
api.add_resource(QueryFoodById, '/queryById/', endpoint='queryFoodById')
api.add_resource(AddFood, '/add/', endpoint='addFood')
api.add_resource(DeleteFood, '/delete/', endpoint='deleteFood')
api.add_resource(UpdateFood, '/update/', endpoint='updateFood')
