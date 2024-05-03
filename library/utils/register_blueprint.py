from ..controller.account_controller import accounts
from ..controller.user_controller import users
from ..controller.calories_controller import calories
from ..controller.water_controller import water
from ..auth.auth_controller import auth
from ..mail.mail_controller import mail
from ..data.import_data import data

def register_blueprint(app):
	app.register_blueprint(users)
	app.register_blueprint(accounts)
	app.register_blueprint(auth)
	app.register_blueprint(mail)
	app.register_blueprint(data)
	app.register_blueprint(water)
	app.register_blueprint(calories) 

