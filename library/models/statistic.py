from ..extension import db	

class Statistic(db.Model):
	__tablename__ = 'statistic'
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	date = db.Column(db.String(255), default=db.func.current_timestamp, primary_key=True)
	morning_calo = db.Column(db.Integer)
	noon_calo = db.Column(db.Integer)
	dinner_calo = db.Column(db.Integer)
	snack_calo = db.Column(db.Integer)
	exercise_calo = db.Column(db.Integer)
	water = db.Column(db.Integer)

	def __init__(self, user_id, morning_calo, noon_calo, dinner_calo, snack_calo, exercise_calo, water):
		self.user_id = user_id
		self.morning_calo = morning_calo
		self.noon_calo = noon_calo
		self.dinner_calo = dinner_calo
		self.snack_calo = snack_calo
		self.exercise_calo = exercise_calo
		self.water = water

	def get_user_statistic_details(self):
		user_details = {
            'user_id': self.user_id,
            'morning_calo': self.morning_calo,
            'noon_calo': self.noon_calo,
            'dinner_calo': self.dinner_calo,
            'snack_calo': self.snack_calo,
            'exercise_calo': self.exercise_calo,
			'water': self.water,
            'total_calo': self.morning_calo  + self.noon_calo + self.dinner_calo + self.snack_calo - self.exercise_calo,
            'date': str(self.date),
        }
		return user_details