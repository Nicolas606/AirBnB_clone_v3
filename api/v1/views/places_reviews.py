#!/usr/bin/python3
""" Place_reviews """

from sqlalchemy.sql.elements import Null
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.place import Place
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def reviews(place_id):
    """  Retrieves the list of all Reviews objects of a State """
    all_reviews = storage.get(Place, place_id)

    if all_reviews == Null:
        abort(404)

    list_reviews = []
    for review in all_reviews.places:
        list_reviews.append(review.to_dict())

    return jsonify(list_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def reviews_id(review_id):
    """ Retrieves a Review object. """
    id_reviews = storage.get(Review, review_id)

    if id_reviews == Null:
        abort(404)

    return jsonify(id_reviews)


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """ Deletes a Review object """
    review_delete = storage.get(Review, review_id)

    if review_delete == Null:
        abort(404)

    storage.delete(review_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """ Creates a review object """


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """ Updates a Place oreview object """
