from flask_jwt_extended import (create_access_token, 
								create_refresh_token, 
								jwt_required, 
								get_jwt_identity,
								get_jwt,
								decode_token
								)
from flask import jsonify
from ..services.account_services import (add_account_services, 
										 get_account_by_email_services, 
										 get_account_by_username_and_password_services)
from datetime import timedelta
from ..services.user_services import add_user_services, get_user_by_account_id_services, get_username_by_account_id
from ..services.account_services import authenticate
from ..mail.mail_services import send_mail
from .blocklist import BLOCKLIST
import random
from cryptography.fernet import Fernet
from ..config import FERNET_KEY
import time, base64


key = FERNET_KEY

sk = base64.urlsafe_b64encode(key.encode())
fernet = Fernet(sk)


def create_otp():
	otp = random.randint(0, 999999)
	otp = str(otp).zfill(6)
	return otp

def encrypt_otp_token(otp, token):
	otp = str(otp)
	token = str(token)
	expiredtime = int(time.time()) + 305
	combined = f'{otp}:{token}:{expiredtime}'.encode()
	encrypted = fernet.encrypt(combined)
	return encrypted.decode()

def decrypt(encrypted):
	decrypted = fernet.decrypt(encrypted.encode()).decode()
	otp, token, expiredtime = decrypted.split(':')
	return otp, token, expiredtime

@jwt_required()
def otp_required_again():
	user = get_jwt_identity()
	email = user['email']
	username = user['username']
	otp = create_otp()
	access_token = create_access_token(identity=user, expires_delta=timedelta(minutes=15))
	encrypt_string = encrypt_otp_token(otp, access_token)
	send_mail("Activate your HealthBuddy account", [email], otp, username)
	return jsonify({
		'message': 'OTP sent to your email', 
		'encrypted': encrypt_string, 
		'token': {
			'access_token': access_token}
	}), 200

@jwt_required()
def otp_authenticated(otp_given, encrypted):
	user = get_jwt_identity()
	otp, token, expiredtime = decrypt(encrypted)
	if int(expiredtime) < int(time.time()):
		return jsonify({'message': 'OTP is expired'}), 401
	else:
		otpIsValid = otp == otp_given
		if not otpIsValid:
			return jsonify({'message': 'Invalid OTP'}), 401
		else:
			email_from_token = user['email']
			email_from_token_given = decode_token(token)['sub']['email']
			if email_from_token == email_from_token_given:
				authenticate(email_from_token)
				return jsonify({'message': 'OTP is valid', 'code': "200", "status": "successfully"}), 200
			else:
				return jsonify({'message': 'Invalid otp from email'}), 401

def login(email, password):
	account = get_account_by_username_and_password_services(email, password)
	username = get_username_by_account_id(account.id)
	if account and username:
		accounts = {
			'account_id': account.id,
			'email': account.email,
			'created_at': account.created_at,
			'username': username
		}
		access_token = create_access_token(identity=accounts, expires_delta=timedelta(minutes=15))
		refresh_token = create_refresh_token(identity=accounts, expires_delta=timedelta(weeks=1))
		return jsonify({
			'message': 'Logged in as {}'.format(username),
			'token': {
				'access_token': access_token,
				'refresh_token': refresh_token},
			'code': 200
		}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

def register(username, email, password):
	emails = [email]
	response = add_account_services(email, password)
	if response != 0:
		account_id = response['account_id']
		result = add_user_services(username, account_id)
		response['username'] = username
		access_token = create_access_token(identity=response, expires_delta=timedelta(minutes=15))
		refresh_token = create_refresh_token(identity=response, expires_delta=timedelta(weeks=1))
		otp = create_otp()
		encrypt_string = encrypt_otp_token(otp, access_token)
		if result:
			send_mail("Activate your HealthBuddy account", emails, otp, username)
			return jsonify({
				'message': 'Account created successfully', 
				'token': {
					'access_token': access_token,
					'refresh_token': refresh_token},
				'encrypted': encrypt_string,
			}), 201
		else:
			return jsonify({'message': 'Account created successfully but failed to create user'}), 201
	else:
		return jsonify({'message': 'Account already exists'}), 409

@jwt_required(refresh=True)
def refresh_token():
	identity = get_jwt_identity()
	access_token = create_access_token(identity=identity, expires_delta=timedelta(minutes=15))
	return jsonify({'access_token': access_token}), 200

@jwt_required()
def getUserInfoByToken():
	user = get_jwt_identity()
	account_id = user['account_id']
	data = get_user_by_account_id_services(account_id)
	return jsonify({
		"message": "Authenticated as {}".format(user['username']),
		"data": data,
		"code": 200,
	})

@jwt_required(refresh=True)
def logout():
	jti = get_jwt()['jti']
	BLOCKLIST.add(jti)
	return jsonify({'message': 'Logout successfully'}), 200

@jwt_required(refresh=True)
def login_by_refresh_token():
	identity = get_jwt_identity()
	access_token = create_access_token(identity=identity, expires_delta=timedelta(minutes=15))
	return jsonify({
		'message': "Logged in as {} with refresh token".format(identity['username']),
		'access_token': access_token,
		'code': 200
	}), 200

@jwt_required()
def get_token():
	token = get_jwt_identity()
	return jsonify(token), 200

@jwt_required(refresh=True)
def read():
	token = get_jwt()
	return jsonify(token), 200