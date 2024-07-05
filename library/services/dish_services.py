from ..extension import db
from ..library_ma import DishSchema
from ..models.dish import Dish
from sqlalchemy import func
import re

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash
from ..services.subscription_services import check_subscription_services

dish_schema = DishSchema()
dishes_schema = DishSchema(many=True)

# def get_all_dishes_services(userID):
# 	if check_subscription_services(userID) == False:
# 		dishes = Dish.query.filter_by(is_premium=0).all()
# 	else:
# 		dishes = Dish.query.all()
# 	result = dishes_schema.dump(dishes)
# 	if not result:
# 		return jsonify({
# 			'message': 'No dishes found'
# 		}), 404
# 	return jsonify({
# 		'dishes': result,
# 		'message': 'success'
# 	}), 200

def get_all_dishes_services(userID, page, page_size):
    page = int(request.args.get('page', 1))  # Lấy giá trị page từ request, mặc định là 1
    page_size = int(request.args.get('page_size', 10))  # Lấy giá trị page_size từ request, mặc định là 10
    offset = (page - 1) * page_size

    if check_subscription_services(userID) == False:
        total_dish = Dish.query.filter_by(is_premium=0).count()
        dishes = Dish.query.filter_by(is_premium=0).offset(offset).limit(page_size).all()
    else:
        total_dish = Dish.query.count()
        dishes = Dish.query.offset(offset).limit(page_size).all()
    result = dishes_schema.dump(dishes)
    total_pages = (total_dish + page_size - 1) // page_size
    
    pagination_metadata = {
        "current_page": page,
        "page_size": page_size,
        "total_items": total_dish,
        "total_pages": total_pages
    }
    response = {
        "dishes": result,
		"pagination": pagination_metadata,
        "message": "success"
    }
    return jsonify(response)

def get_recommend_dish_by_name(name):
    dishes = Dish.query.all()
    
    # Regular expression to match the exact word "cá"
    pattern = re.compile(rf'\b{name}\b', re.IGNORECASE)
    
    # Filter dishes where the name contains the exact word "cá"
    filtered_dishes = [dish for dish in dishes if pattern.search(dish.name)]
    
    # Convert to array of dictionary
    result = dishes_schema.dump(filtered_dishes)
    if not result:
        return False
    return result
