from flask import Blueprint
from flask_restful import Api
from details import InventoryMethods,CategoryMethods, AddUser,Login
from model import AddDetail,Categories,Users



api_bp= Blueprint("api",__name__)
api=Api(api_bp)


api.add_resource(InventoryMethods,"/adddetail")
api.add_resource(InventoryMethods,"/adddetail/<string:category>",endpoint="adddetail")
api.add_resource(CategoryMethods,"/categories",endpoint="categories")
api.add_resource(AddUser,"/adduser")
api.add_resource(Login,"/login")
