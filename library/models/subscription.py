from ..extension import db

class Subcription(db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	is_activate = db.Column(db.Boolean, default=False)
	start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
	is_paid = db.Column(db.Boolean, default=False)
	cost = db.Column(db.Float, nullable=True)

	def __init__(self, user_id, cost):
		self.user_id = user_id
		self.cost = cost
