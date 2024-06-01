from ..extension import db
from flask import jsonify

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=True)
	age = db.Column(db.Integer, nullable=True)
	height = db.Column(db.Integer, nullable=True)
	weight = db.Column(db.Float, nullable=True)
	gender = db.Column(db.String(100), nullable=True)
	exercise = db.Column(db.String(100), nullable=True)
	aim = db.Column(db.String(100), nullable=True)
	disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'), nullable=True)
	is_deleted = db.Column(db.Boolean, default=False)
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
	
	def __init__(self, username, account_id):
		self.username = username
		self.account_id = account_id    
		
	def __repr__(self):
		return f'<User {self.username}>'

	def get_id(self):
		return self.id

	def get_aim(self):
		return self.aim
    
	def get_disease_id(self):
		return self.disease_id

	def calculate_bmi(self):
		bmi = (self.weight / ((self.height / 100) ** 2))
		return bmi

	def calculate_bmr(self):
		if self.gender == 'male':
			bmr = int(10 * int(self.weight) + 6.25 * self.height - 5 * self.age + 5)
		elif self.gender == 'female':
			bmr = int(10 * int(self.weight) + 6.25 * self.height - 5 * self.age - 161)
		else:
			return jsonify({'error': 'Invalid gender'})
		return bmr
    
	def calculate_tdee(self):
		tdee_multiplier = 1.2  
		if self.exercise == 'Vận động nhẹ (1-3 ngày/tuần)':
			tdee_multiplier = 1.375
		elif self.exercise == 'Vận động vừa phải (4-5 ngày/tuần)':
			tdee_multiplier = 1.55
		elif self.exercise == 'Vận động nhiều (6-7 ngày/tuần)':
			tdee_multiplier = 1.9
		bmr = self.calculate_bmr()
		tdee = int(bmr * tdee_multiplier)
		return tdee
	    
	def get_user_details(self):		# Add your code here
		bmi = self.calculate_bmi()
		bmr = self.calculate_bmr()
		tdee = self.calculate_tdee()
  
		user_details = {
			'user_id': self.id,
            'username': self.username,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'gender': self.gender,
            'exercise': self.exercise,
            'aim': self.aim,
            'bmi': bmi,
            'bmr': bmr,
            'tdee': tdee
		}
		return user_details

	def is_validate_user_data(self):
		if self.age == 0 or self.height == 0 or self.weight == 0:
			return False
		return True