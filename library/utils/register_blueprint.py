from ..controller.account_controller import accounts
from ..controller.user_controller import users
from ..auth.auth_controller import auth
def register_blueprint(app):
	app.register_blueprint(users)
	app.register_blueprint(accounts)
	app.register_blueprint(auth)