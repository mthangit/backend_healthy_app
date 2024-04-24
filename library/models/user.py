from ..extension import db

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
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	def __init__(self, username, account_id):
		self.username = username
		self.account_id = account_id
