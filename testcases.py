import requests
import json
import time
from datetime import datetime

app_port=5000

server = "http://localhost:" + str(app_port)

def adduser(first_name,last_name,email):

    data = {
        "first_name":first_name,
        "last_name":last_name,
        "email":email
        }
    
    r = requests.post(server+"/inventory/adduser",json = data)
    
    if "response" in r.json():
        print (email , " user created\n")
        return r.json()["user_id"]
    else:
        print(r.json()["message"])
    return None



def get_adduser():

    r = requests.get(server+"/inventory/adduser")

    if "response" in r.json():
        print(r.json()) 
    else:
        print(r.json()["message"])
    return None



        
def categories(category_name):
    
    data={
        "category_name":category_name
        }
    r = requests.post(server+"/inventory/categories",json = data)

    if "response" in r.json():
        print(r.json())
        print(category_name,"category added")
    else:
        print(r.json()["message"])
    return None



def get_categories():
    r=requests.get(server+"/inventory/categories")

    if "response" in r.json():
        print(r.json())
    else:
        print(r.json()["message"])
    return None

def login(email,password):

    data={"email":email,
            "password":password
    }
    r=requests.post(server+"/inventory/login",json=data)

    if "response" in r.json():
        print(r.json())
    else:
        print(r.json()["messsage"])
    return None

def inventory(purchase_value,vendor_name,stock_id,invoice_no,user_name,date_of_purchase,location):

    data={"purchase_value":purchase_value,
            "vendor_name":vendor_name,"stock_id":stock_id,"invoice_no":invoice_no,"user_name":user_name,
            "date_of_purchase":date_of_purchase,"location":location
    }

    r=requests.post(server+"/inventory/addetail",json=data)

    if "response" in r.json():
        print(r.json())
    else:
        print(r.json()["message"])
    return None

def get_inventory():

    # if category:
    #     r=requests.get(server+"/inventory/addetail/<string:category>")
    #     if "response" in r.json():
    #         print(r.json())

    
    r=requests.get(server+"/inventory/addetail/")
    if "response" in r.json():
        print(r.json())
    return None

get_categories()