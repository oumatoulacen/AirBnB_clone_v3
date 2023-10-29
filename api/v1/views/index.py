#!/usr/bin/python3
''' create routs for views'''
from api.v1.views import app_views
from flask import jsonify


from api.v1.views import app_views


@app_views.route("/status")
def status():
    """api status"""
    return jsonify({"status": "OK"})
