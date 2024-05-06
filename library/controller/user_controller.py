from flask import jsonify, request, Blueprint
from ..services.user_services import add_user_services, update_user_services, get_user_services



users = Blueprint('users', __name__)

# @users.route('/user', methods=['GET'])
# def get_users():
# 	if 'id' in request.args:
# 		id = request.args['id']
# 		return get_user_services(id)
# 	else:
# 		return jsonify({'message': 'No user_id provided'}), 404


# @users.route('/users', methods=['GET'])
# def get_user():
# 	if 'account_id' in request.args:
# 		account_id = request.args['account_id']
# 		return get_all_users_by_account_id_services(account_id)
# 	else:
# 		return get_all_users_services()


@users.route('/api/update-user', methods=['POST'])
def update_user():
	age = request.json.get('age')
	weight = request.json.get('weight')
	height = request.json.get('height')
	aim = request.json.get('aim')
	gender = request.json.get('gender')
	return update_user_services(age, weight, height, gender, aim)


@users.route('/api/calculate', methods=['POST'])
def calculate():
	a = request.json.get('a')
	b = request.json.get('b')
	return jsonify({'result': a + b})

@users.route('/api/get-user', methods=['GET'])
def get_user():
	return get_user_services()