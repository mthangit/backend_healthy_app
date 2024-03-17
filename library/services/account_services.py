from ..extension import db
from ..library_ma import AccountSchema
from ..model import Account
from flask import request, jsonify

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

def get_all_account_services():
	return jsonify(accounts_schema.dump(Account.query.all()))

def get_account_by_username_and_password_services(email, password):
	account = Account.query.filter_by(email=email, password=password).first()
	return account if account else None

def add_account_services(email, password):
	if Account.query.filter_by(email=email).first():
		return 0
	else:
		new_account = Account(email, password)
		db.session.add(new_account)
		db.session.commit()
		return 1
