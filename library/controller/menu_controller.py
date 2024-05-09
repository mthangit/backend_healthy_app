from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.menu_services import get_menu
from flask_jwt_extended import jwt_required, get_jwt_identity

menus = Blueprint('menus', __name__)

@menus.route('/api/get-menu', methods=['GET'])
@jwt_required()
def get_menu_controller():
    try:
        account_id = get_jwt_identity()['account_id']
        if not account_id:
            return jsonify({'message': 'Account not found'}), 404
        menu = get_menu(account_id)
        if menu:
            return jsonify(menu), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
