from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask import Flask, jsonify, request, Blueprint
from ..services.account_services import get_account_by_username_and_password_services, add_account_services




def login(email, password):
	account = get_account_by_username_and_password_services(email, password)
	# Create the JWT token with account and expiration time using JWT_SECRET_KEY
	if account:
		access_token = create_access_token(identity=account.id, expires_delta=False)
		refresh_token = create_refresh_token(identity=account.id, expires_delta=False)
		return jsonify({
			'message': 'Logged in as {}'.format(account.email),
			'token': {
				'access_token': access_token,
				'refresh_token': refresh_token}
		}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401


def register(email, password):
	respone = add_account_services(email, password)
	if respone == 1:
		access_token = create_access_token(identity=email, expires_delta=False)
		refresh_token = create_refresh_token(identity=email, expires_delta=False)
		return jsonify({'message': 'Account created successfully', 'token': {
			'access_token': access_token,
			'refresh_token': refresh_token
		}}), 201
	else:
		return jsonify({'message': 'Account already exists'}), 409
