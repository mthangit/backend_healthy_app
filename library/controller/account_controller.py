from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.account_services import account_exists, get_account_by_email_services
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib
from ..config import SECRET_KEY
accounts = Blueprint('accounts', __name__)


@accounts.route('/api/get-account', methods=['GET'])
def get_account():
	email = request.args.get('email')
	return get_account_by_email_services(email)

@accounts.route('/api/check-account', methods=['GET'])
def check_account():
	email = request.args.get('email')
	result = account_exists(email)
	if result:
		return jsonify({'exists': 'true'}), 200
	else:
		return jsonify({'exists': 'false'}), 404

# @accounts.route('/api/add-account', methods=['POST'])
# def get_account():
# 	email = request.json.get('email')
# 	password = request.json.get('password')
# 	return add_account_services(email, password)

@accounts.route('/hash', methods=['POST'])
def hash_password():
	password = request.json.get('password')
	#hash with secret key using sha256
	sha256 = hashlib.sha256()
	sha256.update(SECRET_KEY.encode('utf-8'))
	sha256.update(password.encode('utf-8'))
	return jsonify({'hash': sha256.hexdigest()})