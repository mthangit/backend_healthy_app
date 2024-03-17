from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.account_services import get_all_account_services, add_account_services


accounts = Blueprint('accounts', __name__)

@accounts.route('/accounts', methods=['GET'])
@jwt_required()
def get_all_accounts():
	return get_all_account_services()


