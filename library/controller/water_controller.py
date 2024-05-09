from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.water_services import save_water, get_user_water_data

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
