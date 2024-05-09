from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.calories_services import save_calories_data, get_user_calories_data
from datetime import datetime  # Thêm dòng này để import module datetime


calories = Blueprint('calories', __name__)

@calories.route('/api/save-calories', methods=['POST'])
@jwt_required()
def save_calories():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        print("Received data :", account_id)  # In ra dữ liệu được gửi từ Postman
        # Trích xuất các trường dữ liệu từ request JSON
        date = data.get('date')  # Lấy ngày từ dữ liệu JSON
        morning_calo = data.get('morning_calo')
        noon_calo = data.get('noon_calo')
        dinner_calo = data.get('dinner_calo')
        snack_calo = data.get('snack_calo')
        exercise_calo = data.get('exercise_calo')
        
        # Chuyển đổi ngày từ string sang datetime object
        # Chuyển đổi ngày từ string sang datetime object
        if date:
             provided_date = datetime.strptime(date, '%Y-%m-%d').date()
        else:
             provided_date = datetime.now().date()

        # Lưu dữ liệu calo vào cơ sở dữ liệu
        save_calories_data(account_id,provided_date, morning_calo, noon_calo, dinner_calo, snack_calo, exercise_calo)
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