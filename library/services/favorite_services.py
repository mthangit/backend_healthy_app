from ..extension import db
from ..library_ma import FavoriteSchema
from ..models.favorite import Favorite
from ..models.dish import Dish
from ..models.user import User
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)


@jwt_required()
def add_favorite_food(user_id, dish_id):
	try:
		new_favorite = Favorite(user_id=user_id, dish_id=dish_id, value=1)
		db.session.add(new_favorite)
		db.session.commit()
		favorites = Favorite.query.filter_by(user_id=user_id).all()
		dish_ids = [fav.dish_id for fav in favorites]
		result = [dish_id for dish_id in dish_ids]
		return jsonify({
			'favorites': result,
			'message': 'Thêm món ăn vào danh sách yêu thích'
		}), 200
	except Exception as e:
		db.session.rollback()
		return jsonify({
			'message': 'Lỗi xảy ra'
		}), 500

@jwt_required()
def delete_favorite(user_id, dish_id):
	try:
		favorite = Favorite.query.filter_by(user_id=user_id, dish_id=dish_id).first()
		if not favorite:
			return False
		favorite.value = 0
		db.session.commit()
		favorites = Favorite.query.filter_by(user_id=user_id).all()
		dish_ids = [fav.dish_id for fav in favorites]
		result = [dish_id for dish_id in dish_ids]
		return jsonify({
			'favorites': result,
			'message': 'Xoá khỏi danh sách yêu thích'
		}), 200
	except Exception as e:
		db.session.rollback()
		return jsonify({
			'message': 'Lỗi xảy ra'
		}), 500
	

@jwt_required()
def get_favorite_by_user_id_services(user_id):
	favorites = Favorite.query.filter_by(user_id=user_id, value=1).all()
	dish_ids = [fav.dish_id for fav in favorites]
	result = [dish_id for dish_id in dish_ids]
	return jsonify({
		'favorites': result,
		'message': 'success'
	}), 200


@jwt_required()
def get_4_name_fav_by_user_id_services(user_id):
	favorites = Favorite.query.filter_by(user_id=user_id).limit(4).all()
	dish_ids = [fav.dish_id for fav in favorites]
	result = [Dish.query.get(dish_id).name for dish_id in dish_ids]
	return jsonify({
		'favorites': result,
		'message': 'success'
	}), 200

@jwt_required()
def get_fav_list_by_user_id(user_id):
	# join dish and favorite table, get all dish information of user_id
	favorites = Favorite.query.join(Dish, Favorite.dish_id == Dish.id).add_columns(Dish.id, Dish.name, Dish.calo, Dish.carb, Dish.fat, Dish.protein).filter(Favorite.user_id == user_id).all()	
	result = []
	for fav in favorites:
		result.append({
			'id': fav.id,
			'name': fav.name,
			'calo': fav.calo,
			'carb': fav.carb,
			'fat': fav.fat,
			'protein': fav.protein
		})
	return jsonify({
		'favorites': result,
		'message': 'success'
	}), 200	
