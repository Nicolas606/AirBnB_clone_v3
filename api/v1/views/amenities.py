#!/usr/bin/python3
""" Amenities """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities():
    """  endpoint that retrieves the list of all Amenity objects """
    all_amenities = storage.all(Amenity).values()
    new = []
    for each_one in all_amenities:
        new.append(each_one.to_dict())
    return jsonify(new)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def amenities_id(amenity_id):
    """  endpoint that Retrieves a Amenity object according to its id """
    all_amenities_id = storage.get(Amenity, amenity_id)
    if all_amenities_id == Null:
        abort(404)
    return jsonify(all_amenities_id)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenities(amenity_id):
    """ Deletes a Amenity object """
    amenitie_delete = storage.get(Amenity, amenity_id)

    if amenitie_delete == Null:
        abort(404)

    storage.delete(amenitie_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenities():
    """ Creates a Amenity object """


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenities(amenity_id):
    """ Updates a Amenity object """
