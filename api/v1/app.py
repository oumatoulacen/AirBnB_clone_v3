#!/usr/bin/python3
""" AirBnB v3 flask Api v1 entrypoint """
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS
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
    """ returns a 404 error
    """
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    ''' endpoint for API'''
    h = getenv("HBNB_API_HOST")
    p = getenv("HBNB_API_PORT")
    host = "0.0.0.0" if h is None else h
    port = "5000" if p is None else p
    app.run(host=host, port=port, threaded=True)
