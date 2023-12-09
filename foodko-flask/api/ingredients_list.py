from flask import request, jsonify
import uuid
from flask import Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt
from models.init_sqlalchemy import db
from models import IngredientsList
from ulit.result import ReBase


ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients/')


class QueryAllIngredients(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        # 获取全部元素
        ingredients_list = IngredientsList.query.all()
        # 将数据转换为数组
        ingredients_arr = []
        for element in ingredients_list:
            ingredients_arr.append(element.to_dict())

        # 使用 jsonify 函数将数据转换为 JSON 格式并传递给前端
        return ReBase('1', obj=ingredients_arr).print()
        pass


class QueryIngredientById(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        id = request.args.get('id')
        ingredients_bp = []
        ingredients_list = []
        if id:
            ingredients_list.append(IngredientsList.query.filter_by(id=id).first())
        else:
            ingredients_list = IngredientsList.query.all()
            pass
        for element in ingredients_list:
            ingredients_bp.append(element.to_dict())

        return ReBase('1', obj=ingredients_bp).print()


class AddIngredient(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # 生成id uuid1=根据MAC地址和时间戳生成
        id = str(uuid.uuid1())
        name = data['name']
        nutrition_list = data['nutrition_list']
        cook_list = data['cook_list']
        alias = data['alias']
        image = data['image']
        main_text = data['main_text']
        icon = data['icon']

        ingredients = IngredientsList(id=id, name=name, nutrition_list=nutrition_list, cook_list=cook_list, alias=alias, image=image, main_text=main_text, icon=icon)
        db.session.add(ingredients)
        db.session.commit()
        return ReBase('1', '添加成功!', obj=ingredients.to_dict()).print()


class DeleteIngredient(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        ids = data['ids']
        for id in ids:
            ingredients = IngredientsList.query.filter_by(id=id).first()
            # print(ingredients, '找到了没有', id)
            if ingredients:
                db.session.delete(ingredients)
        db.session.commit()
        return ReBase('1', '删除成功!').print()


class UpdateIngredient(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        id = data['id']
        name = data['name']
        nutrition_list = data['nutrition_list']
        cook_list = data['cook_list']
        alias = data['alias']
        image = data['image']
        main_text = data['main_text']
        icon = data['icon']

        ingredients = IngredientsList.query.filter_by(id=id).first()
        ingredients.name = name
        ingredients.nutrition_list = nutrition_list
        ingredients.cook_list = cook_list
        ingredients.alias = alias
        ingredients.image = image
        ingredients.main_text = main_text
        ingredients.icon = icon
        db.session.commit()
        return ReBase('1', '修改成功!', obj=ingredients.to_dict()).print()


api = Api(ingredients_bp)
api.add_resource(QueryAllIngredients, '/queryAll/', endpoint='queryAllIngredients')
api.add_resource(QueryIngredientById, '/queryById/', endpoint='queryIngredientById')
api.add_resource(AddIngredient, '/add/', endpoint='addIngredient')
api.add_resource(DeleteIngredient, '/delete/', endpoint='deleteIngredient')
api.add_resource(UpdateIngredient, '/update/', endpoint='updateIngredient')
