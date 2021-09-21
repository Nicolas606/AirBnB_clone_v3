#!/usr/bin/python3
""" Amenities """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort, request
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


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def amenities_id(amenity_id):
    """  endpoint that Retrieves a Amenity object according to its id """
    all_amenities_id = storage.get(Amenity, amenity_id)
    if all_amenities_id == Null:
        abort(404)
    return jsonify(all_amenities_id.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
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
    json = request.get_json()
    if not json:
        abort(400, description="Not a JSON")
    if 'name' not in json:
        abort(400, description="Missing name")

    amenity_object = Amenity(**json)
    amenity_object.save()
    return jsonify(amenity_object.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenities(amenity_id):
    """ Updates a Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")
    for key, value in json.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
