from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.dish_services import get_all_dishes_services
from ..collaborative_filtering.collaborative_filtering import CollaborativeFiltering
from ..models.account import Account
from ..models.meal import Meal
from ..models.dish import Dish

dishes = Blueprint('dishes', __name__)	


@dishes.route('/api/get-all-dishes', methods=['GET'])
@jwt_required()
def get_all_dishes():
	user = get_jwt_identity()
	page = request.args.get('page', 1)
	page_size = request.args.get('page_size', 10)
	return get_all_dishes_services(user['account_id'], page, page_size)

@dishes.route("/total_nutrition/<id>", methods=["GET"])
def total_nutrition(id):
    dish = Dish.query.filter_by(id=id).first()
    if dish:
        total_nutrition = dish.to_dict()
        return total_nutrition
    else:
        return jsonify({'message': 'Dish not found'}), 404
    
@dishes.route("/api/recommend_dish", methods=["GET"])
@jwt_required()
def recommend_dish():
    account_id = get_jwt_identity()['account_id']
    user_account = Account.query.filter_by(id = account_id).first()
    if not user_account:
        return jsonify({'message': 'Unauthorized'}), 404
    CF = CollaborativeFiltering(user_account.id, 3)
    recommend_dish_id = CF.generate_recommendations()
    page = int(request.args.get('page', 1))
    main_category = request.args.get('main_category', '').strip()
    page_size = 4
    offset = (page - 1) * page_size
    if main_category:
        filtered_recommend_dish_id = [dish_id for dish_id in recommend_dish_id if Dish.query.filter_by(main_category=main_category, id=dish_id).first()]
        total_dish = len(filtered_recommend_dish_id)
        total_pages = (total_dish + page_size - 1) // page_size
        list_recommend_dish = [Dish.query.get(dish_id).to_dict() for dish_id in filtered_recommend_dish_id[offset:offset+page_size]]
    else:
        total_dish = len(recommend_dish_id)
        list_recommend_dish = [Dish.query.get(dish_id).to_dict() for dish_id in recommend_dish_id[offset:offset+page_size]]
        total_pages = (total_dish + page_size - 1) // page_size
        
    pagination_metadata = {
        "current_page": page,
        "page_size": page_size,
        "total_items": total_dish,
        "total_pages": total_pages
    }
    response = {
        "data": list_recommend_dish,
        "pagination": pagination_metadata
    }
    return jsonify(response)
