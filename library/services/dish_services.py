from ..extension import db
from ..library_ma import DishSchema
from ..models.dish import Dish
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash

dish_schema = DishSchema()
dishes_schema = DishSchema(many=True)

@jwt_required()
def get_all_dishes_services():
	dishes = Dish.query.all()
	result = dishes_schema.dump(dishes)
	if not result:
		return jsonify({
			'message': 'No dishes found'
		}), 404
	return jsonify({
		'dishes': result,
		'message': 'success'
	}), 200