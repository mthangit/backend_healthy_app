from ..extension import db

class SuggestedMenu(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
	fitness_score = db.Column(db.Integer, nullable=True)
	date_suggest = db.Column(db.DateTime, default=db.func.current_timestamp())
	num_suggest = db.Column(db.Integer, nullable=True)

	def __init__(self, user_id, fitness_score, num_suggest):
		self.user_id = user_id
		self.fitness_score = fitness_score
		self.num_suggest = num_suggest
