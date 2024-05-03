from ..extension import db 

class Ingredient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=True)
	calo = db.Column(db.Float, nullable=True)
	carb = db.Column(db.Float, nullable=True)
	fat = db.Column(db.Float, nullable=True)
	protein = db.Column(db.Float, nullable=True)
	canxi = db.Column(db.Float, nullable=True)
	img = db.Column(db.String(255), nullable=True)
	category = db.Column(db.String(255), nullable=True)

	def __init__(self, name, calo, carb, fat, protein, canxi, category):
		self.name = name
		self.calo = calo
		self.carb = carb
		self.fat = fat
		self.protein = protein
		self.canxi = canxi
		self.category = category


