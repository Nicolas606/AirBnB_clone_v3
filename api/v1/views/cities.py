#!/usr/bin/python3
""" Cities """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """ Retrieves the list of all City objects of a State """
    states_id = storage.get(State, state_id)
    if states_id is None:
        abort(404)
    list_city = []
    all_cities = storage.all(City)
    for city in all_cities:
        if city.state_id == state_id:
            list_city.append(city.to_dict())

    return jsonify(list_city)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_citie(city_id):
    """ Retrieves a City object. """
    all_cities = storage.get(City, city_id)

    if all_cities is None:
        abort(404)

    return jsonify(all_cities)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_cities(city_id):
    """ Deletes a City object """
    city_delete = storage.get(City, city_id)

    if city_delete is None:
        abort(404)

    storage.delete(city_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_cities(state_id):
    """ Creates a City object """
    state_new = storage.get(State, state_id)
    if state_new is None:
        abort(404)

    json = request.get_json()
    if not json:
        abort(400, description="Not a JSON")
    if 'name' not in json:
        abort(400, description="Missing name")

    city_object = City(**json)
    city_object.state_id = state_id
    city_object.save()
    return jsonify(city_object.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_cities(city_id):
    """ Updates a City object """
    cities_id = storage.get(City, city_id)
    if city_id is None:
        abort(404)

    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")
    for key, value in json.item():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(cities_id, key, value)
    storage.save()
    return jsonify(cities_id.to_dict()), 200
