from ..extension import db
from ..library_ma import AccountSchema
from ..model import Account
from flask import request, jsonify

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

def get_all_account_services():
	return jsonify(accounts_schema.dump(Account.query.all()))

