from flask import jsonify, request, Blueprint
from ..services.user_services import get_user_services, add_user_services, get_all_users_by_account_id_services, get_all_users_services


users = Blueprint('users', __name__)

@users.route('/user', methods=['GET'])
def get_users():
	if 'id' in request.args:
		id = request.args['id']
		return get_user_services(id)
	else:
		return jsonify({'message': 'No user_id provided'}), 404


@users.route('/users', methods=['GET'])
def get_user():
	if 'account_id' in request.args:
		account_id = request.args['account_id']
		return get_all_users_by_account_id_services(account_id)
	else:
		return get_all_users_services()



@users.route('/add-user', methods=['POST'])
def add_user():
	return add_user_services()