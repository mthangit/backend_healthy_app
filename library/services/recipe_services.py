from ..extension import db
from ..library_ma import RecipeSchema
from ..models.recipe import Recipe
from ..models.ingredient import Ingredient
from ..models.dish import Dish
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash
from ..services.ingredient_services import get_ingredient_by_id_services

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)


@jwt_required()
def get_recipe_by_dish_id(dish_id):
	recipes = Recipe.query.filter_by(dish_id=dish_id).all()
	list_ingredient = []
	if recipes:
		for recipe in recipes:
			ingredient_details = recipe.get_recipe_detail()
			list_ingredient.append(ingredient_details)
		return list_ingredient
	else:
		return jsonify({'message': 'Recipe not found'}), 404
