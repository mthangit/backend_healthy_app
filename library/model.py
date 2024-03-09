from .extension import db

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	author = db.Column(db.String(100), nullable=False)
	year = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime, server_default=db.func.now())
	updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year
		