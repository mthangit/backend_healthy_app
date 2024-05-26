from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.dish_services import get_all_dishes_services

dishes = Blueprint('dishes', __name__)	


@dishes.route('/api/get-all-dishes', methods=['GET'])
@jwt_required()
def get_all_dishes():
	user = get_jwt_identity()
	page = request.args.get('page', 1)
	page_size = request.args.get('page_size', 10)
	return get_all_dishes_services(user['account_id'], page, page_size)