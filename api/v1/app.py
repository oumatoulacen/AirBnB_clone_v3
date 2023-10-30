#!/usr/bin/python3
""" AirBnB v3 flask Api v1 entrypoint """
from flask import Flask, make_response
from flask_cors import CORS
import json
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)


app.register_blueprint(app_views)
app.url_map.strict_slashes = False
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(err):
    from models import storage
    """api teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    res = {'error': "Not found"}
    response = make_response(json.dumps(res), 404)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == "__main__":
    ''' endpoint for API'''
    h = getenv("HBNB_API_HOST")
    p = getenv("HBNB_API_PORT")
    host = "0.0.0.0" if h is None else h
    port = "5000" if p is None else p
    app.run(host=host, port=port, threaded=True)
