#!/usr/bin/python3
''' Create a new view for Amenity objects'''

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    ''' Retrieves the list of all Amenity objects'''
    amenities = storage.all(Amenity).values()
    amenities_obj = [amenity. to_dict() for amenity in amenities]
    return jsonify(amenities_obj), 200


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    ''' Retrieves a amenity objects from the database'''
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return abort(404)
    amenity_dict = amenity.to_dict()
    return jsonify(amenity_dict), 200


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    ''' deletes an Amenity objects from the database'''
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    ''' create an Amenity objects'''
    json_data = request.get_json()
    if not json_data:
        return abort(400, "Not a JSON")
    if 'name' not in json_data:
        abort(400, "Missing name")
    amenity = Amenity(**json_data)
    amenity.save()
    amenity_dict = amenity.to_dict()
    return jsonify(amenity_dict), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """ update an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404, "Not found")
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
