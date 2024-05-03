from ..controller.account_controller import accounts
from ..controller.user_controller import users
from ..controller.calories_controller import calories  # Import calories_controller
from ..auth.auth_controller import auth
from ..mail.mail_controller import mail

def register_blueprint(app):
	app.register_blueprint(users)
	app.register_blueprint(accounts)
	app.register_blueprint(auth)
	app.register_blueprint(mail)
	app.register_blueprint(calories)  # Đăng ký blueprint calories