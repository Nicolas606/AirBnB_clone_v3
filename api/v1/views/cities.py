#!/usr/bin/python3
""" Cities """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """ Retrieves the list of all City objects of a State """
    states_id = storage.get(State, state_id)

    if states_id == Null:
        abort(404)

    list_cities = []
    for citie in state_id.cities:
        list_cities.append(citie.to_dict())

    return jsonify(list_cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def cities(city_id):
    """ Retrieves a City object. """
    all_cities = storage.get(City, city_id)

    if all_cities == Null:
        abort(404)

    return jsonify(all_cities)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_cities(city_id):
    """ Deletes a City object """
    city_delete = storage.get(City, city_id)

    if city_delete == Null:
        abort(404)

    storage.delete(city_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_cities():
    """ Creates a City object """


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_cities(city_id):
    """ Updates a City object object """
