#!/usr/bin/python3
""" App """
from os import environ
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close(self):
    """ call store.close """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error """
    return jsonify(error="Not found"), 404

if __name__ == '__main__':
    """ Main """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host=host, port=port, threaded=True)
