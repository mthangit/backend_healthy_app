from flask import jsonify, request, Blueprint
from .auth_services import login, register, login_by_refresh_token, refresh_token, getUserInfoByToken, get_token, logout, otp_authenticated, read, otp_required_again
from cryptography.fernet import Fernet
from ..config import FERNET_KEY
import time, base64




key = FERNET_KEY

sk = base64.urlsafe_b64encode(key.encode())
fernet = Fernet(sk)

auth = Blueprint('auth', __name__)

@auth.route('/decrypt', methods=['POST'])
def decrypt():
	data = request.json.get('encrypted')
	encrypted = data.encode()
	decrypted = fernet.decrypt(encrypted)
	return jsonify({'decrypted': decrypted.decode()}), 200

@auth.route('/encrypt', methods=['POST'])
def encrypt():
	data = request.json.get('data')
	encrypted = fernet.encrypt(data.encode())
	return jsonify({'encrypted': encrypted.decode()}), 200


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

@auth.route('/api/logout', methods=['POST'])
def logout_user():
	return logout()

@auth.route('/api/otp-authenticated', methods=['POST'])
def otp_auth():
	otp = request.json.get('otp')
	encrypted = request.json.get('encrypted')
	return otp_authenticated(otp, encrypted)

@auth.route('/api/test', methods=['GET'])
def test():
	return jsonify({'message': FERNET_KEY}), 200


@auth.route('/api/read-token', methods=['GET'])
def read_token():
	return read()

@auth.route('/api/otp-required-again', methods=['POST'])
def otp_required():
	return otp_required_again()