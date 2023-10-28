#!/usr/bin/python3
''' create views blueprints'''
from flask import Blueprint
from api.v1.views.index import *

# flake8: noqa

app_views = Blueprint('bp_views', __name__, url_prefix='/api/v1')
