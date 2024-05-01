#!/usr/bin/python3
'''API status'''

from flask import Flask, jsonify
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage


app = Flask(__name__)


@app_views.route('/status')
def api_status():
    '''Return API status'''
    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats')
def api_stats():
    '''Return JSON Responses'''
    stats = {
        'amenities': storage.count('Amenities'),
        'cities': storage.count('Cities'),
        'places': storage.count('Places'),
        'reviews': storage.count('Reviews'),
        'states': storage.count('States'),
        'users': storage.count('Users')
    }
    return jsonify(stats)
