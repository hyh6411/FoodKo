from flask import request, jsonify
import uuid
from flask import Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt
from models.init_sqlalchemy import db
from models import ElementList
from ulit.result import ReBase


element_bp = Blueprint('element', __name__, url_prefix='/element/')


class QueryAllElement(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        # 获取全部元素
        element_list = ElementList.query.all()
        # 将数据转换为数组
        element_arr = []
        for element in element_list:
            element_arr.append(element.to_dict())

        # 使用 jsonify 函数将数据转换为 JSON 格式并传递给前端
        return ReBase('1', obj=element_arr).print()
        pass


class QueryElement(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        id = request.args.get('id')
        element_bp = []
        element_list = []
        if id:
            element_list.append(ElementList.query.filter_by(id=id).first())
        else:
            element_list = ElementList.query.all()
            pass
        for element in element_list:
            element_bp.append(element.to_dict())

        return ReBase('1', obj=element_bp).print()


class AddElement(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        # 生成id uuid1=根据MAC地址和时间戳生成
        id = str(uuid.uuid1())
        name = data['name']
        chemical_tag = data['chemical_tag']
        main_text = data['main_text']
        alias = data['alias']
        image = data['image']
        link = data['link']
        icon = data['icon']
        origin_food = data['origin_food']
        origin_select = data['origin_select']
        compute = data['compute']
        heat = data['heat']
        back_color = data['back_color']

        element = ElementList(id=id, name=name, chemical_tag=chemical_tag, main_text=main_text, alias=alias, image=image, link=link,
                              icon=icon, origin_food=origin_food, origin_select=origin_select, compute=compute, heat=heat, back_color=back_color)
        db.session.add(element)
        db.session.commit()
        return ReBase('1', '添加成功!', obj=element.to_dict()).print()


class DeleteElement(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        ids = request.get_json()['ids']
        for id in ids:
            element = ElementList.query.filter_by(id=id).first()
            if element:
                db.session.delete(element)
        db.session.commit()
        return ReBase('1', '删除成功!').print()


class UpdateElement(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        id = data['id']
        name = data['name']
        chemical_tag = data['chemical_tag']
        main_text = data['main_text']
        alias = data['alias']
        image = data['image']
        link = data['link']
        icon = data['icon']
        origin_food = data['origin_food']
        origin_select = data['origin_select']
        compute = data['compute']
        heat = data['heat']
        back_color = data['back_color']

        element = ElementList.query.filter_by(id=id).first()
        element.name = name
        element.chemical_tag = chemical_tag
        element.main_text = main_text
        element.alias = alias
        element.image = image
        element.link = link
        element.icon = icon
        element.origin_food = origin_food
        element.origin_select = origin_select
        element.compute = compute
        element.heat = heat
        element.back_color = back_color
        db.session.commit()
        return ReBase('1', '修改成功!', obj=element.to_dict()).print()


api = Api(element_bp)
api.add_resource(QueryAllElement, '/queryAllElement/', endpoint='queryAllElement')
api.add_resource(QueryElement, '/queryElement/', endpoint='queryElement')
api.add_resource(AddElement, '/addElement/', endpoint='addElement')
api.add_resource(DeleteElement, '/deleteElement/', endpoint='deleteElement')
api.add_resource(UpdateElement, '/updateElement/', endpoint='updateElement')




