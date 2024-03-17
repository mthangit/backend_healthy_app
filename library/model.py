from .extension import db

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), nullable=True)
	password = db.Column(db.String(100), nullable=True)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

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

	def __init__(self, username, age, height, weight, gender, exercise, aim, is_deleted, account_id):
		self.username = username
		self.age = age
		self.height = height
		self.weight = weight
		self.gender = gender
		self.exercise = exercise
		self.aim = aim
		self.is_deleted = is_deleted	
		self.account_id = account_id

