#!/usr/bin/python3
"""api index"""
from api.v1.views import app_views


@app_views.route("/status")
def status():
    """api status"""
    return {"status": "OK"}
