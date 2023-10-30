#!/usr/bin/python3
""" AirBnB v3 flask Api v1 entrypoint """
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")
CORS(app)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(err):
    """api teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """ returns a 404 error
    """
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    ''' endpoint for API'''
    host = "0.0.0.0" if host is None else host
    port = "5000" if port is None else port
    app.run(host=host, port=port, threaded=True)
