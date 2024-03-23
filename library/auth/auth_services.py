from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from flask import Flask, jsonify
from ..services.account_services import add_account_services, get_account_by_email_services, get_account_by_username_and_password_services
from datetime import timedelta
from ..services.user_services import add_user_services, get_user_by_account_id_services, get_username_by_account_id

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
	response = add_account_services(email, password)
	if response != 0:
		account_id = response['account_id']
		result = add_user_services(username, account_id)
		response['username'] = username
		access_token = create_access_token(identity=response, expires_delta=timedelta(minutes=15))
		refresh_token = create_refresh_token(identity=response, expires_delta=timedelta(weeks=1))
		if result:
			return jsonify({
				'message': 'Account created successfully', 
				'token': {
					'access_token': access_token,
					'refresh_token': refresh_token},
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
	return get_user_by_account_id_services(account_id)

def logout():
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