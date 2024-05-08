from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.favorite_services import add_favorite_food, delete_favorite, get_favorite_by_user_id_services, get_4_name_fav_by_user_id_services

favorites = Blueprint('favorite', __name__)

@favorites.route('/api/change-favorite', methods=['POST'])
@jwt_required()
def add_favorite():
	user_id = request.json['user_id']
	dish_id = request.json['dish_id']
	type = request.json['type']
	if type == 1:
		return add_favorite_food(user_id, dish_id)
	else:
		return delete_favorite(user_id, dish_id)


@favorites.route('/api/get-favorite-by-user-id/<user_id>', methods=['GET'])
def get_favorite_by_user_id(user_id):
	return get_favorite_by_user_id_services(user_id)

@favorites.route('/api/get-home-fav/<user_id>', methods=['GET'])
def get_4_name_fav_by_user_id(user_id):
	return get_4_name_fav_by_user_id_services(user_id)