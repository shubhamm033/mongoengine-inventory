from flask import request,jsonify
from flask_restful import Resource
from model import AddDetail, db,Categories, CategorySchema, AddDetailsSchema,Users,UserSchema,LoginSchema
import json
import hashlib
import faker
import jwt
from config import jwt_secret
from auth import auth
from cors import crossdomain
import uuid

categories_schema= CategorySchema(many=True)
categories_schema= CategorySchema()

details_schema=AddDetailsSchema(many=True)
details_schema=AddDetailsSchema()

user_schema=UserSchema()
login_schema=LoginSchema()

class InventoryMethods(Resource):
    #@auth
    @crossdomain(origin="*")
    def get(self,category=None):

        
        if category:
            details=AddDetail.objects(category=category)
            return jsonify({"response":details})
        
        
        else:
            details = AddDetail.objects.all()
            return jsonify({"response": details})



    #@auth
    @crossdomain(origin="*")
    def post(self):

        json_data=request.get_json(force=True)
        
        if not json_data:
            return jsonify({"response":"No data provided"})

        data, errors =details_schema.load(json_data)

        if errors:
            return errors

        AddDetail(**json_data).save()
        return jsonify({ "response": "success"})

    def delete(self):
        json_data=request.get_json(force=True)
        if not json_data:
            return jsonify({"message":"not selected"})
        data, errors = details_schema.load(json_data)
        
        if errors:
            return errors

        detail = AddDetail.objects(stock_id=data["stock_id"])
        
        if detail:
            detail.delete()

        return jsonify({"response":"successfully deleted"})

    def put(self):
        json_data=request.get_json(force=True)
        
        if not json_data:
            return jsonify({"response":"Not data provided"})

        data,error= details_schema.load(json_data)

        if error:
            return error
        

        stock_id = AddDetail.objects(stock_id=data["stock_id"])


        if not stock_id:
            return jsonify({"response": " can not be updated"})
        
        
        Categories(**json_data).update()
        return jsonify({"response":"success"})





class CategoryMethods(Resource):
    #@auth
    @crossdomain(origin="*")
    def get(self):

        all_categories = Categories.objects.all()
        return jsonify({"response": all_categories})
    
    @crossdomain(origin="*")
    def post(self):
        json_data=request.get_json(force=True)
        

        if not json_data:
            return jsonify({"message":"no data provided"})

        data, errors = categories_schema.load(json_data)
        
        if errors:
            return errors
        
        category = Categories.objects(category_name=data["category_name"])
        
        if category:
            return jsonify({"message": "category already exists"})
        
        
        Categories(**json_data).save()
        return jsonify({"response":"success"})
        

    def delete(self):
        json_data=request.get_json(force=True)
        if not json_data:
            return jsonify({"response":"category not selected"})

        data, errors = categories_schema.load(json_data)
        
        if errors:
            return errors

        category = Categories.objects(Category_Name=data["Category_Name"])
        
        if category:
            category.delete()


            return jsonify({"response":"successfully deleted"})

        return jsonify({"message":"category not found"})
    
    def put(self):
        json_data=request.get_json(force=True)
        
        if not json_data:
            return jsonify({"response":"Not data provided"})

        data,error= category_schema.load(json_data)

        if error:
            return error
        

        category = Categories.objects(Category_Name=data["Category_Name"])


        if not category:
            return jsonify({"response": "category can't be updated"})
        
        
        Categories(**json_data).update()
        return jsonify({"response":"success"})


    


        







class AddUser(Resource):
    @crossdomain(origin="*")
    def get(self):
        all_users=Users.objects.all()
        return jsonify({"response":all_users})

    @auth
    @crossdomain(origin="*")
    def post(self):
    
        json_data=request.get_json(force=True)
        
        if not json_data:
            return jsonify({"message":"no data provided"})

        data,errors= user_schema.load(json_data)

        if errors:
            return errors
            
        user_email = data.get("email").decode("utf-8")
            
        if not user_email:
            return jsonify({"message":"please enter your details"})



        user_exist=  Users.objects(email=user_email)
        
        if user_exist:
            return jsonify({"message":"user already exists"})
        
        else:
            uid = uuid.uuid4().hex
            pass_id = user_email.split("@")[0]
            password = hashlib.sha256(pass_id.encode("utf-8")).hexdigest()

            new_user={"email":user_email,
                        "password":password,
                        "user_id":uid}


            Users(**new_user).save()
            return jsonify({"response":"user added"})

    def delete(self):
        json_data=request.get_json(force=True)
        if not json_data:
            return jsonify({"response":"user not selected"})
        
        data, errors = user_schema.load(json_data)
        
        if errors:
            return errors

        user_exist = Users.objects(purchase_value=data["purchase_value"])
    
        if user_exist:
            user_exist.delete()


            return jsonify({"response":"successfully deleted"})

        return jsonify({"message":"user not found"})


class Login(Resource):
    @auth
    @crossdomain(origin="*")
    def get(self):
        print(request.headers)
        
        return jsonify({"response":"success"}) 
    
    def post(self):
        json_data=request.get_json(force=True)
        

        if not json_data:
            return jsonify({"message":"please enter details"})
        
        data,errors= login_schema.load(json_data)
        
        if errors:
            return errors
            
            
        user_email = data.get("email").decode("utf-8")
        user_password=data.get("password").decode("utf-8")
            
        if not user_email or not user_password:

            return jsonify({"message":"please enter proper details"})
            
        password = hashlib.sha256(user_password.encode("utf-8")).hexdigest()
        user = Users.objects.get(email=user_email)
            
        if not user:
            return jsonify({"message":"user is not registerd"})
            
        else:
            if user.password != password:
                return jsonify({"message":"incorrect password"})
            
            else:
                f = faker.Faker()

                token_json = {
                         #f.address() : f.sentences(),
                        "_id": user["user_id"]
                        }
                
                token =  jwt.encode(token_json, jwt_secret, algorithm="HS256")
                return jsonify({"response":"successs","token": token})

