from api.view import Test
from flask_restful import Api
from flask import Blueprint

api = Blueprint("api", __name__) # 设置蓝图
resource = Api(api)
resource.add_resource(Test, "/shopee/test") # 设置路由