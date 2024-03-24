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

