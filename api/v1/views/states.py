#!/usr/bin/python3
''' Create a new view for State objects that
andles all default RESTFul API actions'''

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import make_response, abort, request
import json

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    ''' Retrieves the list of all State objects'''
    states = storage.all(State).values()
    states_obj = [state.to_dict() for state in states]
    res = make_response(json.dumps(states_obj), 200)
    res.headers['Content-Type'] = 'application/json'
    return res


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    ''' Retrieves a State objects from the database'''
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    state_dict = state.to_dict()
    res = make_response(json.dumps(state_dict), 200)
    res.headers['Content-Type'] = 'application/json'
    return res


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    ''' deletes a State objects from the database'''
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    storage.delete(state)
    storage.save()
    state_dict = {}
    res = make_response(json.dumps(state_dict), 200)
    res.headers['Content-Type'] = 'application/json'
    return res


@app_views.route('/states', methods=['POST'])
def create_state(state_id):
    ''' create a State objects'''
    json_data = request.get_json()
    if json_data:
        return abort(400, "Not a JSON")
    if 'name' not in json_data:
        abort(400, "Missing name")
    state = State(**json_data)
    state.save()
    state_dict = state.to_dict()
    res = make_response(json.dumps(state_dict), 201)
    res.headers['Content-Type'] = 'application/json'
    return res


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ update a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404, "Not found")
    if not request.json:
        abort(400, "Not a JSON")
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in request.json.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200