# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 08:13:32 2021

@author: gendutkiy
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests


''' db conection'''
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://gendutkiy:spidey34.@27.112.79.65:5432/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

''' table product '''
class ProductTab(db.Model):
     __tablename__ = "product"
     __table_args__ = {"schema": "public"}
     product_id=db.Column(db.String(), primary_key=True)
     product_name = db.Column(db.String())
     category = db.Column(db.String())

     def __init__(self,pr_id,pr_nm,cat):
         self.product_id = pr_id
         self.product_name =pr_nm
         self.category =cat

''' table user '''        
class UserTab(db.Model):
     __tablename__ = "user"
     __table_args__ = {"schema": "public"}
     user_id=db.Column(db.String(), primary_key=True)
     user_name = db.Column(db.String())
     email = db.Column(db.String())

     def __init__(self,us_id,us_nm,eml):
         self.user_id = us_id
         self.user_name =us_nm
         self.email =eml


''' table order '''        
class OrderTab(db.Model):
     __tablename__ = "order"
     __table_args__ = {"schema": "public"}
     order_id=db.Column(db.String(), primary_key=True)
     user_id = db.Column(db.String())
     product_id = db.Column(db.String())
     num_order = db.Column(db.String())

     def __init__(self,or_id,us_id,pr_id,ttl):
         self.order_id = or_id
         self.user_id =us_id
         self.product_id =pr_id
         self.num_order =ttl

''' check status '''  
@app.route('/status',methods=['Get'])
def status():
    return jsonify({'status':'OK'})


''' get data table product '''
@app.route("/product/<pro_id>", methods=["GET", "POST"])
def GetProduct(pro_id):
    if request.method == 'GET' :
        try :
            prod_data=ProductTab.query.all()
            result= [{
                'product_id' : a.product_id,
                'product_name' : a.product_name,
                'category' : a.category
                } for a in prod_data]
            return jsonify(result)
        except Exception as e :
            raise e
    elif request.method == 'POST' :
        data_prod=request.get_json()
        prodc=ProductTab(
                pr_id=data_prod.get('product_id'),
                pr_nm=data_prod.get('product_name'),
                cat=data_prod.get('category'))
        db.session.add(prodc)
        db.session.commit()

        return {"message": f"product_id {data_prod['product_id']}  added"}
    
  
''' get data table user '''
@app.route("/user/<usr_id>", methods=["GET", "POST"])
def GetUser(usr_id):
    if request.method == 'GET' :
        try :
            user_data=UserTab.query.all()
            result= [{
                'user_id' : a.user_id,
                'user_name' : a.user_name,
                'email' : a.email
                } for a in user_data]
            return jsonify(result)
        except Exception as e :
            raise e
    elif request.method == 'POST' :
        data_user=request.get_json()
        useradd=UserTab(
                us_id=data_user.get('user_id'),
                us_nm=data_user.get('user_name'),
                eml=data_user.get('email'))
        db.session.add(useradd)
        db.session.commit()

        return {"message": f"user_id {data_user['user_id']}  added"}
    
''' get data table order '''
@app.route("/order/<odr_id>", methods=["GET", "POST"])
def GetOrder(odr_id):
    if request.method == 'GET' :
        try :
            order_data=OrderTab.query.all()
            result= [{
                'order_id' : a.order_id,
                'user_id' : a.user_id,
                'product_id' : a.product_id,
                'num_order' : a.num_order
                } for a in order_data]
            return jsonify(result)
        except Exception as e :
            raise e
    elif request.method == 'POST' :
        data_order=request.get_json()
        orderadd=OrderTab(
                or_id=data_order.get('order_id'),
                us_id=data_order.get('user_id'),
                pr_id=data_order.get('product_id'),
                ttl=data_order.get('num_order'))
        db.session.add(orderadd)
        db.session.commit()

        return {"message": f"order_id {data_order['order_id']}  added"}


if __name__ == "__main__":
    app.run(debug=True, port=5060)


