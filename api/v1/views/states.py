#!/usr/bin/python3
""" States """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states():
    """  endpoint that retrieves the list of all State objects """
    states = storage.all(State).values()
    new = []
    for each_one in states:
        new.append(each_one.to_dict())
    return jsonify(new)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def states_id(state_id):
    """  endpoint that Retrieves a state object according to its id """
    states_id = storage.get(State, state_id)
    if states_id is None:
        abort(404)
    return jsonify(states_id.to_dict())


@app_views.route('/sates/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_states(state_id):
    """ Deletes a State object """
    state_delete = storage.get(State, state_id)

    if state_delete is None:
        abort(404)

    storage.delete(state_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Creates a State """
    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")
    if 'name' not in json:
        abort(400, description="Missing name")

    state_object = State(**json)
    state_object.save()

    return jsonify(state_object.to_dict()), 201



@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State onject"""
    state_obj = storage.get(State, state_id)

    if state_obj is None:
        abort(404)

    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")

    for key, value in json.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state_obj, key, value)
    storage.save()
    return jsonify(state_obj.to_dict()), 200
