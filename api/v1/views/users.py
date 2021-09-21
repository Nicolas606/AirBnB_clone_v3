#!/usr/bin/python3
""" Users """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """  endpoint that retrieves the list of all User objects """
    all_users = storage.all(User).values()
    new = []
    for each_one in all_users:
        new.append(each_one.to_dict())
    return jsonify(new)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def users_id(user_id):
    """  endpoint that Retrieves a User object according to its id """
    all_users_id = storage.get(User, user_id)
    if all_users_id == Null:
        abort(404)
    return jsonify(all_users_id.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a User object """
    user_delete = storage.get(User, user_id)

    if user_delete == Null:
        abort(404)

    storage.delete(user_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_users():
    """ Creates a State object"""
    json = request.get_json()
    if not json:
        abort(400, description="Not a JSON")
    if 'email' not in json:
        abort(400, description="Missing email")
    if 'password' not in json:
        abort(400, description="Missing password")

    user_object = User(**json)
    user_object.save()
    return jsonify(user_object.to_dict()), 201


@app_views.route('users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_users(user_id):
    """ Updates a State object"""
    users_id = storage.get(User, user_id)
    if users_id is None:
        abort(404)

    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")
    for key, value in json.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(users_id, key, value)
    storage.save()
    return jsonify(users_id.to_dict()), 200
