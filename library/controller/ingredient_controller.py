from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.ingredient_services import get_all_ingredients_services

ingredients = Blueprint('ingredients', __name__)

@ingredients.route('/api/get-all-ingredients', methods=['GET'])
def get_all_ingredients():
	return get_all_ingredients_services()