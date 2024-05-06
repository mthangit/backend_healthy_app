from ..extension import db
from ..library_ma import AccountSchema
from ..models.account import Account
from ..models.user import User
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy import text

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
		return None
	
def account_exists(email):
	acc = Account.query.filter_by(email=email).first()
	return True if acc else False

def authenticate(email):
	account = Account.query.filter_by(email=email).first()
	account.authenticated = True
	db.session.commit()
	return True 

def change_password(email, password):
	# account = Account.query.filter_by(email=email).first()
	# account.password = generate_password_hash(password).decode('utf-8')
	print(email)
	print(password)
	db.session.query(Account).filter(Account.email == email).update({Account.password: generate_password_hash(password).decode('utf-8')})
	db.session.commit()
	return True

def get_info_by_email(email):
	#join account and user table to get user info by email
	sql = text("select email, username, user.account_id, created_at from account join user on account.id = user.account_id where email = :email")
	result = db.session.execute(sql, {'email': email}).fetchone()
	return {
		'email': result[0],
		'username': result[1],
		'account_id': result[2],
		'created_at': result[3]
	}

@jwt_required()
def get_info_by_account_id():
	account_id = get_jwt_identity()['account_id']
	#join account and user table to get user info by account_id
	sql = text("select email, username, user.account_id, created_at, authenticated from account join user on account.id = user.account_id where user.account_id = :account_id")
	result = db.session.execute(sql, {'account_id': account_id}).fetchone()
	return {
		'email': result[0],
		'username': result[1],
		'account_id': result[2],
		'created_at': result[3],
		'authenticated': result[4]
	}