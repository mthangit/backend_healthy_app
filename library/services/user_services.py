from ..extension import db
from ..library_ma import UserSchema
# from ..model import User
from ..models.user import User
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .subscription_services import get_subscription_by_user_id_services, user_has_subscription_services

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def add_user_services(username, account_id):
	try:
		new_user = User(username=username, account_id=account_id)
		db.session.add(new_user)
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		return False

def get_user_by_account_id_services(id):
	user = User.query.filter_by(account_id=id).first()
	if user is None:
		return None
	return (user_schema.dump(user))

def get_username_by_account_id(id):
	user = User.query.filter_by(account_id=id).first()
	return user.username if user else None

@jwt_required()
def update_user_services(age, weight, height, gender, aim):
	account_id = get_jwt_identity()['account_id']
	try:
		user = User.query.filter_by(account_id=account_id).first()
		user.age = age
		user.weight = weight
		user.height = height
		user.aim = aim
		user.gender = gender
		db.session.commit()
		return jsonify(user_schema.dump(user)), 200
	except Exception as e:
		db.session.rollback()
		return jsonify({'message': 'Failed to update user'}), 500


@jwt_required()
def get_user_services():
	user = get_jwt_identity()
	account_id = user['account_id']
	data = get_user_by_account_id_services(account_id)
	if data is None:
		return jsonify({'message': 'User not found'}), 404
	# Check if user has subscription
	result = user_has_subscription_services(account_id)
	if result != False:
		data['has_subscription'] = True
		data['expired_date'] = result['expired_date']
	else:
		data['has_subscription'] = False
		data['expired_date'] = None
	return jsonify(data), 200