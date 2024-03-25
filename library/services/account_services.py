from ..extension import db
from ..library_ma import AccountSchema
from ..model import Account
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

def get_account_by_username_and_password_services(email, password):
	account = Account.query.filter_by(email=email).first()
	if account and check_password_hash(account.password, password):
		return account
	else:
		return None

def add_account_services(email, password):
	if Account.query.filter_by(email=email).first():
		return 0
	else:
		pw = generate_password_hash(password).decode('utf-8')
		new_account = Account(email, pw)
		db.session.add(new_account)
		db.session.commit()
		#get id of account
		account = Account.query.filter_by(email=email).first()
		return {
			'account_id': account.id,
			'email': account.email,
			'created_at': account.created_at
		}

def get_account_by_email_services(email):
	account = Account.query.filter_by(email=email).first()
	if account:
		return jsonify({
			'account_id': account.id,
			'email': account.email,
			'created_at': account.created_at
		})
	else:
		return jsonify({'message': 'Account not found'}), 404
	
def account_exists(email):
	return Account.query.filter_by(email=email).first() is not None

def authenticate(email):
	account = Account.query.filter_by(email=email).first()
	account.authenticated = True
	db.session.commit()
	return True 
