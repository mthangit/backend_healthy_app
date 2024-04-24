from ..extension import db

class Menu(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=True)

	def __init__(self, name):
		self.name = name