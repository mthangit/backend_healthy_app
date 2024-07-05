from ..controller.account_controller import accounts
from ..controller.user_controller import users
from ..controller.calories_controller import calories
from ..controller.water_controller import water
from ..controller.ingredient_controller import ingredients
from ..controller.subscription_controller import subscriptions
from ..auth.auth_controller import auth
from ..mail.mail_controller import mail
from ..controller.dish_controller import dishes
from ..controller.recipe_controller import recipes
from ..controller.favorite_controller import favorites
from ..controller.menu_controller import menus
from ..data.import_data import data
from ..detect.detect_services import detect

def register_blueprint(app):
	app.register_blueprint(users)
	app.register_blueprint(accounts)
	app.register_blueprint(auth)
	app.register_blueprint(mail)
	app.register_blueprint(data)
	app.register_blueprint(water)
	app.register_blueprint(calories) 
	app.register_blueprint(dishes)
	app.register_blueprint(subscriptions)
	app.register_blueprint(ingredients)
	app.register_blueprint(recipes)
	app.register_blueprint(favorites)
	app.register_blueprint(menus)
	app.register_blueprint(detect)

