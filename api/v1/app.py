#!/usr/bin/python3
'''start API application'''

from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    '''close the storage'''
    storage.close()


host = environ.get('HBNB_API_HOST')
port = environ.get('HBNB_API_PORT')

if __name__ == "__main__":
    """api entrypoint"""
    port = port if port is not None else 5000
    host = host if host is not None else '0.0.0.0'
    app.run(port=port, host=host, threaded=True)
