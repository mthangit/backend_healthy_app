from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.calories_services import save_calories_morning, get_user_calories_data, save_calories_noon, save_calories_exercise, save_calories_snack, save_calories_dinner
from datetime import datetime  # Thêm dòng này để import module datetime
from ..models.user import User
from ..models.account import Account
from ..models.statistic import Statistic
from datetime import datetime, timedelta
from ..extension import db


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

@calories.route('/api/statistic/get-user-calories', methods=['GET'])
@jwt_required()
def get_user_calories():
        account_id = get_jwt_identity()['account_id']
        print(account_id)
        if not account_id:
            return jsonify({'message': 'No user_id provided'}), 400
        return get_user_calories_data(account_id)
    

@calories.route('/api/statistic/get-sevendays-statistic', methods=["GET"])
@jwt_required()
def sevendays_statistic():
    account_id = get_jwt_identity()['account_id']
    user_account = Account.query.filter_by(id = account_id).first()
    if not user_account:
        return jsonify({'message': 'Unauthorized'}), 404
    user = User.query.get(user_account.id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_details = user.get_user_details()
    num_days = int(request.args.get('days', 7))
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=num_days-1)
    statistics_by_day = []
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        user_statistic = Statistic.query.filter(
            Statistic.user_id == user_account.id,
            db.func.date(Statistic.date) == current_date
        ).all()
        daily_stats = {
            "date": current_date.strftime("%d-%m-%Y"), 
            "total_morning_calo": 0,
            "total_noon_calo": 0,
            "total_dinner_calo": 0,
            "total_snack_calo": 0,
            "total_exercise_calo": 0,
            "total_calo": 0
        }
        if user_statistic:
            daily_stats["total_morning_calo"] = sum(item.morning_calo for item in user_statistic)
            daily_stats["total_noon_calo"] = sum(item.noon_calo for item in user_statistic)
            daily_stats["total_dinner_calo"] = sum(item.dinner_calo for item in user_statistic)
            daily_stats["total_snack_calo"] = sum(item.snack_calo for item in user_statistic)
            daily_stats["total_exercise_calo"] = sum(item.exercise_calo for item in user_statistic)
            daily_stats["total_calo"] = (
                daily_stats["total_morning_calo"] + daily_stats["total_noon_calo"] +
                daily_stats["total_dinner_calo"] + daily_stats["total_snack_calo"] -
                daily_stats["total_exercise_calo"]
            )
        statistics_by_day.append(daily_stats)

    return jsonify({
        "data": statistics_by_day,
        "tdee": user_details["tdee"]
    }), 200

    
