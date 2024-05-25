from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.water_services import save_water, get_user_water_data
from ..models.user import User
from ..models.account import Account
from ..models.statistic import Statistic
from datetime import datetime, timedelta
from ..extension import db

water = Blueprint('water', __name__)

@water.route('/api/statistic/add_water', methods=['POST'])
@jwt_required()
def save_data_water():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        # Trích xuất các trường dữ liệu từ request JSON
        water = data.get('water')
        save_water(account_id, water)
        return jsonify({'message': 'Water data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@water.route('/api/statistic/get-user-water', methods=['GET'])
@jwt_required()
def get_user_water():
    account_id = get_jwt_identity()['account_id']
    if not account_id:
        return jsonify({'message': 'No user_id provided'}), 400
    return get_user_water_data(account_id)

@water.route('/api/statistic/get-sevendays-water', methods=["GET"])
@jwt_required()
def sevendays_water():
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
    water_by_day = []
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        user_statistic = Statistic.query.filter(
            Statistic.user_id == user_account.id,
            db.func.date(Statistic.date) == current_date
        ).all()
        daily_stats = {
            "date": current_date.strftime("%d-%m-%Y"), 
            "total_water": 0
        }
        if user_statistic:
            daily_stats["total_water"] = sum(item.water for item in user_statistic)
        water_by_day.append(daily_stats)
    return jsonify({
        "data": water_by_day,
        "tdee": user_details["tdee"]
    }), 200