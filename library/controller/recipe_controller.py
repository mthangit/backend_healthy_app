from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.recipe_services import get_recipe_by_dish_id

recipes = Blueprint('recipes', __name__)

@recipes.route('/api/get-recipe-by-dish-id/<id>', methods=['GET'])
def get_recipe_by_dish_id_controller(id):
	return jsonify(get_recipe_by_dish_id(id))
