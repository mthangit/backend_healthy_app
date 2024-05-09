from ..extension import db

class Favorite(db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), primary_key=True)
	value = db.Column(db.Integer)

	def __init__(self, user_id, dish_id, value):
		self.user_id = user_id
		self.dish_id = dish_id
		self.value = value
