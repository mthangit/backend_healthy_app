from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.dish_services import get_all_dishes_services

dishes = Blueprint('dishes', __name__)	


@dishes.route('/api/get-all-dishes', methods=['GET'])
def get_all_dishes():
	return get_all_dishes_services()