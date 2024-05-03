from ..extension import db

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), nullable=True)
	password = db.Column(db.String(100), nullable=True)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	authenticated = db.Column(db.Boolean, default=False)
	def __init__(self, email, password):
		self.email = email
		self.password = password
		
