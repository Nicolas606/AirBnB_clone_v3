#!/usr/bin/python3
""" Places """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.city import City
from models.place import Place


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def places(city_id):
    """  Retrieves the list of all Places objects of a State """
    all_places = storage.get(City, city_id)

    if all_places == Null:
        abort(404)

    list_places = []
    for place in all_places.places:
        list_places.append(place.to_dict())

    return jsonify(list_places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def places_id(place_id):
    """ Retrieves a Place object. """
    id_places = storage.get(Place, place_id)

    if id_places == Null:
        abort(404)

    return jsonify(id_places)


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """ Deletes a Place object """
    place_delete = storage.get(City, place_id)

    if place_delete == Null:
        abort(404)

    storage.delete(place_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """ Creates a place object """


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """ Updates a Place object object """
