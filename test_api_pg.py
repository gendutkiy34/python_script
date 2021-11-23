# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:41:22 2021

@author: gendutkiy
"""

from flask import Flask, request, jsonify
from connection_postgress import connection, cursor


app = Flask(__name__)

@app.route("/league", methods=["GET", "POST"])

def league():
    if request.method == "GET":
        query = """
            SELECT * FROM postgres.public.league;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5050)