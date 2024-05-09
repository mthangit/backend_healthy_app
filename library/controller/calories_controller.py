from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.calories_services import save_calories_morning, get_user_calories_data
from datetime import datetime  # Thêm dòng này để import module datetime


calories = Blueprint('calories', __name__)

@calories.route('/api/statistic/add_morning', methods=['POST'])
@jwt_required()
def save_calories():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        morning_calo = data.get('morning_calo')
        save_calories_morning(account_id, morning_calo)
        return jsonify({'message': 'Calories morning data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@calories.route('/api/get-user-calories', methods=['GET'])
def get_user_calories():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'No user_id provided'}), 400
    calories_data = get_user_calories_data(user_id)
    if calories_data:
        return jsonify(calories_data), 200
    else:
        return jsonify({'message': 'No calories data found for this user'}), 404