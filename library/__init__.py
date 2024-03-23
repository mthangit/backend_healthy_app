from flask import Flask, jsonify
from .extension import db, masrhmallow, jwt, bcrypt
from .utils.register_blueprint import register_blueprint
def create_app(config_file = 'config.py'):
	app = Flask(__name__)
	app.config.from_pyfile(config_file)
	bcrypt.init_app(app)
	db.init_app(app)
	masrhmallow.init_app(app)
	with app.app_context():
		db.create_all()
		print('Database created!')
	register_blueprint(app)
	jwt.init_app(app)

	# handling error jwt

	@jwt.invalid_token_loader
	def invalid_token_callback(error):
		return jsonify({
			'description': 'Signature verification failed',
			'error': 'invalid_token'
		}), 401
	
	@jwt.unauthorized_loader
	def missing_token_callback(error):
		return jsonify({
			'description': 'Request does not contain an access token',
			'error': 'authorization_required'
		}), 401
	
	@jwt.expired_token_loader
	def expired_token_callback(jwt_header, jwt_payload):
		return jsonify({
			'description': 'The token has expired',
			'error': 'token_expired'
		}), 401
	return app