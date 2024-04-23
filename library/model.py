from .extension import db

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), nullable=True)
	password = db.Column(db.String(100), nullable=True)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	authenticated = db.Column(db.Boolean, default=False)
	def __init__(self, email, password):
		self.email = email
		self.password = password
		

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=True)
	age = db.Column(db.Integer, nullable=True)
	height = db.Column(db.Integer, nullable=True)
	weight = db.Column(db.Integer, nullable=True)
	gender = db.Column(db.String(100), nullable=True)
	exercise = db.Column(db.String(100), nullable=True)
	aim = db.Column(db.String(100), nullable=True)
	is_deleted = db.Column(db.Boolean, default=False)
	# account_id = db.Interger, db.ForeignKey('account.id'), nullable=False
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	def __init__(self, username, account_id):
		self.username = username
		self.account_id = account_id


# CREATE TABLE IF NOT EXISTS `ingredient` (
#   `id` int NOT NULL AUTO_INCREMENT,
#   `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   `calo` float DEFAULT NULL,
#   `carb` float DEFAULT NULL,
#   `fat` float DEFAULT NULL,
#   `protein` float DEFAULT NULL,
#   `img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


class Ingredient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=True)
	calo = db.Column(db.Float, nullable=True)
	carb = db.Column(db.Float, nullable=True)
	fat = db.Column(db.Float, nullable=True)
	protein = db.Column(db.Float, nullable=True)
	img = db.Column(db.String(255), nullable=True)

	def __init__(self, name, calo, carb, fat, protein):
		self.name = name
		self.calo = calo
		self.carb = carb
		self.fat = fat
		self.protein = protein


# CREATE TABLE IF NOT EXISTS `dish` (
#   `id` int NOT NULL AUTO_INCREMENT,
#   `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   `calo` float DEFAULT NULL,
#   `carb` float DEFAULT NULL,
#   `fat` float DEFAULT NULL,
#   `protein` float DEFAULT NULL,
#   `img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   `is_premium` tinyint(1) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
class Dish(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=True)
	calo = db.Column(db.Float, nullable=True)
	carb = db.Column(db.Float, nullable=True)
	fat = db.Column(db.Float, nullable=True)
	protein = db.Column(db.Float, nullable=True)
	img = db.Column(db.String(255), nullable=True)
	is_premium = db.Column(db.Boolean, default=False)

	def __init__(self, name, calo, carb, fat, protein, img, is_premium):
		self.name = name
		self.calo = calo
		self.carb = carb
		self.fat = fat
		self.protein = protein
		self.img = img
		self.is_premium = is_premium


# CREATE TABLE IF NOT EXISTS `recipe` (
#   `ingredient_id` int NOT NULL,
#   `dish_id` int NOT NULL,
#   `grams` float DEFAULT NULL,
#   PRIMARY KEY (`ingredient_id`,`dish_id`),
#   KEY `dish_id` (`dish_id`),
#   CONSTRAINT `recipe_ibfk_1` FOREIGN KEY (`dish_id`) REFERENCES `dish` (`id`),
#   CONSTRAINT `recipe_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredient` (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
class Recipe(db.Model):
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
	dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), primary_key=True)
	grams = db.Column(db.Float, nullable=True)

	def __init__(self, ingredient_id, dish_id, grams):
		self.ingredient_id = ingredient_id
		self.dish_id = dish_id
		self.grams = grams