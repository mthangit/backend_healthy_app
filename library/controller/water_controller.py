from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.water_services import save_water_data

water = Blueprint('water', __name__)

@water.route('/api/save-water', methods=['POST'])
@jwt_required()
def save_water():
    try:
        account_id = get_jwt_identity()['account_id']
        data = request.json
        print("Received data :", account_id)  # In ra dữ liệu được gửi từ Postman
        # Trích xuất các trường dữ liệu từ request JSON
        water = data.get('water')
        
        # Lưu dữ liệu water vào cơ sở dữ liệu
        save_water_data(account_id, water)
        return jsonify({'message': 'Water data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

