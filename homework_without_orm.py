# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:41:22 2021

@author: gendutkiy
"""

from flask import Flask, request, jsonify
from connection_postgress import connection, cursor


app = Flask(__name__)

''' Check status connection to API '''
@app.route("/status", methods=["GET", "POST"],)
def status_con():
    return jsonify({'status':'OK'})


''' table order '''
@app.route("/order/<ord_id>", methods=["GET", "POST"],)

def order(ord_id):
    if request.method == "GET":
        id_req=f"'{ord_id}'"
        query =f"""
        SELECT * FROM postgres.public.order WHERE order_id={id_req};
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        return jsonify(result)
    
    elif request.method == "POST":
        data = request.get_json()
        query = """
            INSERT INTO postgres.public.order (
                order_id, user_id, product_id,num_order
            ) VALUES (
                %(order_id)s, %(user_id)s, %(product_id)s, %(num_order)s
            );
        """
        cursor.execute(query, data)
        connection.commit()
        
        return jsonify({"message": f"order_id {data.get('order_id')} data has been added"})


''' table product '''
@app.route("/product/<pro_id>", methods=["GET", "POST"],)

def product(pro_id):
    if request.method == "GET":
        pro_id=f"'{pro_id}'"
        query =f"""
        SELECT * FROM postgres.public.product WHERE product_id={pro_id};
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        return jsonify(result)
    elif request.method == "POST":
        data = request.get_json()
        query = """
            INSERT INTO postgres.public.product (
                product_id, product_name, category
            ) VALUES (
                %(product_id)s, %(product_name)s, %(category)s
            );
        """
        cursor.execute(query, data)
        connection.commit()
        
        return jsonify({"message": f"product_id {data.get('product_id')} data has been added"})


''' user product '''
@app.route("/user/<usr_id>", methods=["GET", "POST"],)

def user(usr_id):
    if request.method == "GET":
        us_id=f"'{usr_id}'"
        query =f"""
        SELECT * FROM postgres.public.user WHERE user_id={us_id};
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        return jsonify(result)
    elif request.method == "POST":
        data = request.get_json()
        query = """
            INSERT INTO postgres.public.user (
                user_id, user_name, email
            ) VALUES (
                %(user_id)s, %(user_name)s, %(email)s
            );
        """
        cursor.execute(query, data)
        connection.commit()
        
        return jsonify({"message": f"user_id {data.get('user_id')} data has been added"})


if __name__ == "__main__":
    app.run(debug=True, port=5050)