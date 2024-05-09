from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.calories_services import save_calories_morning, get_user_calories_data, save_calories_noon, save_calories_exercise, save_calories_snack, save_calories_dinner
from datetime import datetime  # Thêm dòng này để import module datetime


calories = Blueprint('calories', __name__)

@calories.route('/api/statistic/add_morning', methods=['POST'])
@jwt_required()
def save_data_calories_morning():
    try:
        account_id = get_jwt_identity()['account_id']
        print(account_id,request.json)
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        morning_calo = data.get('morning_calo')
        print(account_id, morning_calo)
        save_calories_morning(account_id, morning_calo)
        return jsonify({'message': 'Calories morning data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    
@calories.route('/api/statistic/add_noon', methods=['POST'])
@jwt_required()
def save_data_calories_noon():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        noon_calo = data.get('noon_calo')
        save_calories_noon(account_id, noon_calo)
        return jsonify({'message': 'Calories noon data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@calories.route('/api/statistic/add_dinner', methods=['POST'])
@jwt_required()
def save_data_calories_dinner():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        dinner_calo = data.get('dinner_calo')
        save_calories_dinner(account_id, dinner_calo)
        return jsonify({'message': 'Calories dinner data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@calories.route('/api/statistic/add_snack', methods=['POST'])
@jwt_required()
def save_data_calories_snack():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        snack_calo = data.get('snack_calo')
        save_calories_snack(account_id, snack_calo)
        return jsonify({'message': 'Calories snack data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@calories.route('/api/statistic/add_exercise', methods=['POST'])
@jwt_required()
def save_data_calories_exercise():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        exercise_calo = data.get('exercise_calo')
        save_calories_exercise(account_id, exercise_calo)
        return jsonify({'message': 'Calories exercise data saved successfully'}), 200
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