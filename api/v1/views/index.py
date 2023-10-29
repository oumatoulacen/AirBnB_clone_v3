#!/usr/bin/python3
''' create routs for views'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
