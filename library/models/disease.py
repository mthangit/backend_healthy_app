from ..extension import db 

class Disease(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	disease_name = db.Column(db.String(255), nullable=True)

	def __init__(self, name):
		self.name = name

	def get_id(self):
		return self.id
	
	def get_disease_name(self):
		return self.disease_name
