import os
from datetime import datetime
from flask import request, jsonify
import uuid
from flask import Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ulit.result import ReBase


public_bp = Blueprint('public', __name__, url_prefix='/public/')


class UploadImage(Resource):
    # method_decorators = [jwt_required()]

    def post(self):
        f = request.files['file']
        real_path = '/static/images/database/'
        if f and f.filename:
            ext = f.filename.rsplit('.')[-1]
            file_name = str(uuid.uuid1()) + '.' + ext
            f.save(os.path.join('./static/images/database/', file_name))
            file_data = {
                'file_name': file_name,
                'file_path': real_path + file_name,
            }
            return ReBase('1', msg='上传图片成功！', obj=file_data).print()
        else:
            return ReBase('2').print()


class Test(Resource):
    def get(self):
        return ReBase('1', msg="测试").print()


api = Api(public_bp)
api.add_resource(Test, '/test/')
api.add_resource(UploadImage, '/uploadImage')
