from ..extension import db
from ..library_ma import UserSchema
from ..model import User
from flask import request

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def get_user_services(id):
	return user_schema.jsonify(User.query.get(id))

def get_all_users_by_account_id_services(account_id):
	return users_schema.jsonify(User.query.filter_by(account_id=account_id).all())

def get_all_users_services():
	return users_schema.jsonify(User.query.all())

def add_user_services():
	username = request.json['username']
	age = request.json['age']
	height = request.json['height']
	weight = request.json['weight']
	gender = request.json['gender']
	exercise = request.json['exercise']
	aim = request.json['aim']
	is_deleted = request.json['is_deleted']
	account_id = request.json['account_id']

	new_user = User(username, age, height, weight, gender, exercise, aim, is_deleted, account_id)
	db.session.add(new_user)
	db.session.commit()
	return user_schema.jsonify(new_user)