#!/usr/bin/python3
""" Place_reviews """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def reviews(place_id):
    """  Retrieves the list of all Reviews objects of a State """
    place_new = storage.get(Place, place_id)

    if place_new is None:
        abort(404)

    list_reviews = []
    all_reviews = storage.all(Review)
    for review in all_reviews.values():
        if review.place_id == place_id:
            list_reviews.append(review.to_dict())

    return jsonify(list_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def reviews_id(review_id):
    """ Retrieves a Review object. """
    id_reviews = storage.get(Review, review_id)

    if id_reviews is None:
        abort(404)

    return jsonify(id_reviews.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ Deletes a Review object """
    review_delete = storage.get(Review, review_id)

    if review_delete is None:
        abort(404)

    storage.delete(review_delete)
    storage.save()

    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """ Creates a review object """
    reviews = storage.get(Place, place_id)
    if reviews is None:
        abort(404)

    json = request.get_json()
    if not json:
        abort(400, description="Not a JSON")
    if 'user_id' not in json:
        abort(400, description="Missing user_id")
    if storage.get(User, json['user_id']) is None:
        abort(400)
    if 'text' not in json:
        abort(400, description="Missing text")

    review_object = Review(**json)
    review_object.save()
    return jsonify(review_object.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """ Updates a Place oreview object """
    reviews = storage.get(Review, review_id)
    if reviews is None:
        abort(404)

    json = request.get_json()
    if json is None:
        abort(400, description="Not a JSON")
    for key, value in json.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(reviews, key, value)
    storage.save()
    return jsonify(reviews.to_dict()), 200
