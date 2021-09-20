#!/usr/bin/python3
""" States """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort
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
    if states_id == Null:
        abort(404)
    return jsonify(states_id)


@app_views.route('/sates/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_states(state_id):
    """ Deletes a State object """
    state_delete = storage.get(State, state_id)

    if state_delete == Null:
        abort(404)

    storage.delete(state_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/sates', methods=['POST'], strict_slashes=False)
def create_state():
    """ Creates a State """


@app_views.route('/sates/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State """
