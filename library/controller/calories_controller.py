from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.calories_services import save_calories_data, get_user_calories_data

calories = Blueprint('calories', __name__)

@calories.route('/api/save-calories', methods=['POST'])
@jwt_required()
def save_calories():
    try:
        user_id = get_jwt_identity()  # Lấy user_id từ token
        data = request.json
        # Lưu dữ liệu calo vào cơ sở dữ liệu
        save_calories_data(user_id, data)
        return jsonify({'message': 'Calories data saved successfully'}), 200
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