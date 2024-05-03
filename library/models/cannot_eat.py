from ..extension import db 

class CannotEat(db.Model):
	disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'), primary_key=True)
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)

	def __init__(self, disease_id, ingredient_id):
		self.disease_id = disease_id
		self.ingredient_id = ingredient_id
