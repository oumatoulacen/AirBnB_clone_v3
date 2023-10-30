#!/usr/bin/python3
''' Create a new view for User objects'''

from api.v1.views import app_views
from models import storage
from models.user import User
from flask import abort, request, jsonify


@app_views.route('/users', methods=['GET'])
def get_users():
    ''' Retrieves the list of all User objects'''
    users = storage.all(User).values()
    users_obj = [user. to_dict() for user in users]
    return jsonify(users_obj), 200


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    ''' Retrieves a User objects from the database'''
    user = storage.get(User, user_id)
    if not user:
        return abort(404)
    user_dict = user.to_dict()
    return jsonify(user_dict), 200


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    ''' deletes a User objects from the database'''
    user = storage.get(User, user_id)
    if not user:
        return abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'])
def create_user():
    ''' create a User objects'''
    json_data = request.get_json()
    if not json_data:
        return abort(400, "Not a JSON")
    if 'name' not in json_data:
        abort(400, "Missing name")
    user = User(**json_data)
    user.save()
    user_dict = user.to_dict()
    return jsonify(user_dict), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """ update a User"""
    user = storage.get(User, user_id)
    if not user:
        abort(404, "Not found")
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    ignore_keys = ['id', 'created_at', 'email', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
