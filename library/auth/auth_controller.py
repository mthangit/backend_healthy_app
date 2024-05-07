from flask import jsonify, request, Blueprint
from .auth_services import (login, 
							register, 
							login_by_refresh_token, 
							refresh_token, 
							getUserInfoByToken, 
							get_token, 
							logout, 
							read, 
							otp_required, 
							authenticated_otp_reset,
							authenticated_account,
							reset_password)
from cryptography.fernet import Fernet
from ..config import FERNET_KEY
import time, base64
from ..services.account_services import get_account_by_email_services, get_info_by_email
from flask_jwt_extended import jwt_required, get_jwt_identity


key = FERNET_KEY

sk = base64.urlsafe_b64encode(key.encode())
fernet = Fernet(sk)

auth = Blueprint('auth', __name__)

@auth.route('/api/decrypt', methods=['POST'])
def decrypt():
	data = request.json.get('encrypted')
	encrypted = data.encode()
	decrypted = fernet.decrypt(encrypted)
	return jsonify({'decrypted': decrypted.decode()}), 200

@auth.route('/api/encrypt', methods=['POST'])
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

@auth.route('/api/signup', methods=['POST'])
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



@auth.route('/api/test', methods=['GET'])
def test():
	return jsonify({'message': FERNET_KEY}), 200


@auth.route('/api/read-token', methods=['GET'])
def read_token():
	return read()

@auth.route('/api/otp-required', methods=['POST'])
def otp():
	email = request.json.get('email')
	reset = request.json.get('reset')
	if reset == "true":
		resetpass = True
	else:
		resetpass = False
	return otp_required(email, resetpass)

@auth.route('/api/otp-reset-password', methods=['POST'])
def otp_reset_password():
	otp = request.json.get('otp')
	encrypted = request.json.get('encrypted')
	return authenticated_otp_reset(otp, encrypted)

@auth.route('/api/otp-authenticated-account', methods=['POST'])
def otp_auth():
	otp = request.json.get('otp')
	encrypted = request.json.get('encrypted')
	return authenticated_account(otp, encrypted)


@auth.route('/api/reset-password', methods=['POST'])
def reset_password_route():
	password = request.json.get('password')
	print(password)
	return reset_password(password)

@auth.route('/api/check-token', methods=['POST'])	
def check_token():
	return get_token()

@auth.route('/api/user-info', methods=['GET'])  # Thêm endpoint mới để lấy thông tin user_id
@jwt_required()  # Bảo vệ endpoint này bằng JWT, người dùng cần phải đăng nhập để truy cập
def get_user_info():
    user_id = get_jwt_identity()  # Lấy user_id từ token
    return jsonify({'user_id': user_id}), 200