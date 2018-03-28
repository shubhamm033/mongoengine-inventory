import datetime
from flask_mongoengine import MongoEngine
from marshmallow import Schema, fields,pre_load,validate
from flask_marshmallow import Marshmallow
ma=Marshmallow()
db= MongoEngine()


class AddDetail(db.Document):
    purchase_value=db.IntField(reruired=True)
    vendor_name=db.StringField(required=True)
    stock_id=db.StringField(required=True)
    invoice_no=db.IntField(required=True)
    user_name=db.StringField(required=True)
    date_of_purchase=db.DateTimeField(required=True,default=datetime.datetime.now())
    location=db.StringField(required=True)
class AddDetailsSchema(ma.Schema):
    purchase_value=fields.Int()
    vendor_name=fields.String()
    stock_id=fields.String()
    invoice_no=fields.Int()
    #date_of_purchase=fields.DateTime()
    user_name=fields.String()
    location=fields.String()
class Users(db.Document):
    email=db.StringField()
    password=db.StringField()
    user_id=db.StringField()
    first_name=db.StringField()
    last_name=db.StringField()
    

class UserSchema(ma.Schema):
    email=fields.String()
    first_name=fields.String()
    last_name=fields.String()
    
    
class Categories(db.Document):
    category_name=db.StringField()
class CategorySchema(ma.Schema):
    category_name=fields.String()
    

class LoginSchema(ma.Schema):
    email=fields.String()
    password=fields.String()
    





