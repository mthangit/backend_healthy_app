from ..extension import db
from ..library_ma import IngredientSchema
from ..models.ingredient import Ingredient
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)


@jwt_required()
def get_all_ingredients_services():
	ingredients = Ingredient.query.all()
	result = ingredients_schema.dump(ingredients)
	if not result:
		return jsonify({
			'message': 'No ingredients found'
		}), 404
	return jsonify({
		'ingredients': result,
		'message': 'success'
	}), 200


@jwt_required()
def get_ingredient_by_id_services(ingredient_id):
	ingredient = Ingredient.query.get(ingredient_id)
	if not ingredient:
		return jsonify({
			'message': 'Ingredient not found'
		}), 404
	result = ingredient_schema.dump(ingredient)
	return jsonify({
		'ingredient': result,
		'message': 'success'
	}), 200
