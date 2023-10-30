#!/usr/bin/python3
''' Create a new view for city objects'''

from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import abort, request, jsonify


@app_views.route('/states/<id>/cities', methods=['GET'])
def get_cities(id):
    ''' Retrieves a cities objects of a state'''
    state = storage.get(State, id)
    if not state:
        abort(404)
    cities = state.cities
    cities_dict = [city.to_dict() for city in cities]
    return jsonify(cities_dict), 200


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    ''' deletes a State objects from the database'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    ''' delete a city objects from the database'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<s_id>/cities', methods=['POST'])
def create_city(s_id):
    ''' create a city'''
    state = storage.get(State, s_id)
    if not state:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return abort(400, "Not a JSON")
    if 'name' not in json_data:
        abort(400, "Missing name")
    city = City(**json_data)
    city.state_id = s_id
    city.save()
    city_dict = city.to_dict()
    return jsonify(city_dict), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """ update a state"""
    city = storage.get(City, city_id)
    if not city:
        abort(404, "Not found")
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
