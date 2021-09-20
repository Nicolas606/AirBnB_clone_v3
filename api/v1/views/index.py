#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """ returns a JSON: "status": "OK" """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """  endpoint that retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    name = ['amenities', 'cities', 'places', 'reviews', 'states', 'users']
    new_dict = {}

    for i in range(len(classes)):
        new_dict[name[i]] = storage.count(classes[i])

    return jsonify(new_dict)

