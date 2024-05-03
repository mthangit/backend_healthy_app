from ..controller.account_controller import accounts
from ..controller.user_controller import users
from ..controller.subscription_controller import subscriptions
from ..auth.auth_controller import auth
from ..mail.mail_controller import mail
from ..data.import_data import data
def register_blueprint(app):
	app.register_blueprint(users)
	app.register_blueprint(accounts)
	app.register_blueprint(auth)
	app.register_blueprint(mail)
	app.register_blueprint(data)
	app.register_blueprint(subscriptions)