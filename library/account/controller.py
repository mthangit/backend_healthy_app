from flask import jsonify, request, Blueprint
from .services import get_all_account_services


accounts = Blueprint('accounts', __name__)

@accounts.route('/accounts', methods=['GET'])
def get_all_accounts():
	return get_all_account_services()