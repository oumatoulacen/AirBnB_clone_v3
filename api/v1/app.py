#!/usr/bin/python3
""" AirBnB v3 flask Api v1 entrypoint """
from models import storage
from flask import Flask, jsonify
from flask_cors import CORS
import json
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")
app.url_map.strict_slashes = False

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(err):
    """teardown session"""
    storage.close()


@app.errorhandler(404)
def not_found_err(err):
    """ create a 404 Error response:
        description: a resource was not found
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """api entrypoint"""
    host = "0.0.0.0" if host is None else host
    port = "5000" if port is None else port
    app.run(host=host, port=port, threaded=True)
