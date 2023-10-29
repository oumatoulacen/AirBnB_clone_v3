#!/usr/bin/python3
'''start API application'''

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    '''close the storage'''
    storage.close()

host = environ.get('HBNB_API_HOST', '0.0.0.0')
port = environ.get('HBNB_API_PORT', 5000)

if __name__ == "__main__":
    """api entrypoint"""
    app.run(debug=True, port=port, host=host, threaded=True)
