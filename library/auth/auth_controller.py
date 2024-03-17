from flask import jsonify, request, Blueprint
from .auth_services import login, register

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login_route():
	email = request.json.get('email', None)
	password = request.json.get('password', None)
	return login(email, password)


@auth.route('/register', methods=['POST'])
def register_route():
	email = request.json['email']
	password = request.json['password']
	return register(email, password)