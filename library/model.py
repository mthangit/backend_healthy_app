from .extension import db

# class Account(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	email = db.Column(db.String(100), nullable=True)
# 	password = db.Column(db.String(100), nullable=True)
# 	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
# 	authenticated = db.Column(db.Boolean, default=False)
# 	def __init__(self, email, password):
# 		self.email = email
# 		self.password = password
		

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(100), nullable=True)
# 	age = db.Column(db.Integer, nullable=True)
# 	height = db.Column(db.Integer, nullable=True)
# 	weight = db.Column(db.Integer, nullable=True)
# 	gender = db.Column(db.String(100), nullable=True)
# 	exercise = db.Column(db.String(100), nullable=True)
# 	aim = db.Column(db.String(100), nullable=True)
# 	is_deleted = db.Column(db.Boolean, default=False)
# 	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

# 	def __init__(self, username, account_id):
# 		self.username = username
# 		self.account_id = account_id




# class Recipe(db.Model):
# 	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
# 	dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), primary_key=True)
# 	grams = db.Column(db.Float, nullable=True)

# 	def __init__(self, ingredient_id, dish_id, grams):
# 		self.ingredient_id = ingredient_id
# 		self.dish_id = dish_id
# 		self.grams = grams






# class CannotEat(db.Model):
# 	disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'), primary_key=True)
# 	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)

# 	def __init__(self, disease_id, ingredient_id):
# 		self.disease_id = disease_id
# 		self.ingredient_id = ingredient_id

# class Favorite(db.Model):
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
# 	dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), primary_key=True)

# 	def __init__(self, user_id, dish_id):
# 		self.user_id = user_id
# 		self.dish_id = dish_id

# class Subcription(db.Model):
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
# 	is_activate = db.Column(db.Boolean, default=False)
# 	start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
# 	is_paid = db.Column(db.Boolean, default=False)
# 	cost = db.Column(db.Float, nullable=True)

# 	def __init__(self, user_id, cost):
# 		self.user_id = user_id
# 		self.cost = cost

# class SuggestedMenu(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
# 	fitness_score = db.Column(db.Integer, nullable=True)
# 	date_suggest = db.Column(db.DateTime, default=db.func.current_timestamp())
# 	num_suggest = db.Column(db.Integer, nullable=True)

# 	def __init__(self, user_id, fitness_score, num_suggest):
# 		self.user_id = user_id
# 		self.fitness_score = fitness_score
# 		self.num_suggest = num_suggest

# class Menu(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(255), nullable=True)

# 	def __init__(self, name):
# 		self.name = name