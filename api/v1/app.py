#!/usr/bin/python3
'''start API'''
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ

host = environ.get('HBNB_API_HOST', '0.0.0.0')
port = environ.get('HBNB_API_PORT', '5000')
app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    '''close the storage'''
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, port=port, host=host, threaded=True)
