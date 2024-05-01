#!/usr/bin/python3
"""Flask server"""

from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_engine(exception):
    """Teardown app context"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return jsonify(error='Not found'), 404


if __name__ == "__main__":
    # Use environment variables for configuration
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')  # Default to '0.0.0.0'
    PORT = int(getenv('HBNB_API_PORT', 5000))  # Default to port 5000
    app.run(host=HOST, port=PORT, threaded=True, debug=True)
