#!/usr/bin/python3
""" Places """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.user import User
from models.place import Place


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def places(city_id):
    """  Retrieves the list of all Places objects of a State """
    all_places = storage.get(City, city_id)

    if all_places is None:
        abort(404)

    list_places = []
    for place in all_places.places:
        list_places.append(place.to_dict())

    return jsonify(list_places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def places_id(place_id):
    """ Retrieves a Place object. """
    id_places = storage.get(Place, place_id)

    if id_places is None:
        abort(404)

    return jsonify(id_places.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """ Deletes a Place object """
    place_delete = storage.get(Place, place_id)

    if place_delete is None:
        abort(404)

    storage.delete(place_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """ Creates a place object """
    place = storage.get(City, city_id)
    if place is None:
        abort(404)

    json = request.get_json()
    if not json:
        abort(400, description="Not a JSON")
    if 'user_id' not in json:
        abort(400, description="Missing user_id")
    if storage.get(User, json['user_id']) is None:
        abort(400)
    if 'name' not in json:
        abort(400, description="Missing name")


    place_object = Place(**json)
    place_object.city_id = city_id
    place_object.save()
    return jsonify(place_object.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """ Updates a Place object object """
    places = storage.get(Place, place_id)
    if places is None:
        abort(404)

    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")
    for key, value in json.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(places, key, value)
    storage.save()
    return jsonify(places.to_dict()), 200
