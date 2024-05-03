from .extension import db

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), nullable=True)
	password = db.Column(db.String(100), nullable=True)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	authenticated = db.Column(db.Boolean, default=False)
	def __init__(self, email, password):
		self.email = email
		self.password = password
		

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=True)
	age = db.Column(db.Integer, nullable=True)
	height = db.Column(db.Integer, nullable=True)
	weight = db.Column(db.Integer, nullable=True)
	gender = db.Column(db.String(100), nullable=True)
	exercise = db.Column(db.String(100), nullable=True)
	aim = db.Column(db.String(100), nullable=True)
	is_deleted = db.Column(db.Boolean, default=False)
	# account_id = db.Interger, db.ForeignKey('account.id'), nullable=False
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	def __init__(self, username, account_id):
		self.username = username
		self.account_id = account_id

class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    morning_calo = db.Column(db.Integer)
    noon_calo = db.Column(db.Integer)
    dinner_calo = db.Column(db.Integer)
    snack_calo = db.Column(db.Integer)
    exercise_calo = db.Column(db.Integer)
    water = db.Column(db.Integer)

    user = db.relationship('User', backref=db.backref('statistics', lazy=True))

    def __init__(self, user_id, date, morning_calo=None, noon_calo=None, dinner_calo=None, snack_calo=None, exercise_calo=None, water=None):
        self.user_id = user_id
        self.date = date
        self.morning_calo = morning_calo
        self.noon_calo = noon_calo
        self.dinner_calo = dinner_calo
        self.snack_calo = snack_calo
        self.exercise_calo = exercise_calo
        self.water = water
