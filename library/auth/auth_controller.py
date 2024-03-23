from flask import jsonify, request, Blueprint
from .auth_services import login, register, login_by_refresh_token, refresh_token, getUserInfoByToken, get_token

auth = Blueprint('auth', __name__)

@auth.route('/api/login', methods=['POST'])
def login_route():
	refresh_token = request.headers.get('Authorization')
	if refresh_token and refresh_token.startswith('Bearer '):
		return login_by_refresh_token()	
	else:
		email = request.json.get('email', None)
		password = request.json.get('password', None)
		if not email or not password:
			return jsonify({'message': 'Missing email or password parameter'}), 400
		return login(email, password)

@auth.route('/api/authenticate', methods=['GET'])
def authenticate():
	return getUserInfoByToken()

@auth.route('/api/refresh', methods=['POST'])
def refresh():
	return refresh_token()

@auth.route('/api/register', methods=['POST'])
def register_route():
	username = request.json['username']
	email = request.json['email']
	password = request.json['password']
	return register(username, email, password)

@auth.route('/api/get-token-identity', methods=['GET'])
def get_token_identity():
	return get_token()
