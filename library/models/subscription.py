from datetime import datetime, timedelta
from ..extension import db
from dateutil.relativedelta import relativedelta

class Subscription(db.Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	subscription_id = db.Column(db.String, primary_key=True)
	is_activate = db.Column(db.Boolean, default=False)
	start_date = db.Column(db.DateTime)
	is_paid = db.Column(db.Boolean, default=False)
	cost = db.Column(db.Float, nullable=True)
	payment_date = db.Column(db.DateTime, nullable=True)
	# subscription_type is enum type (1: monthly, 2: yearly)
	subscription_type = db.Column(db.Integer, nullable=True)
	expired_date = db.Column(db.DateTime, nullable=True)
	created_date = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, user_id, subscription_id ,cost, subscription_type):
		self.user_id = user_id
		self.subscription_id = subscription_id
		self.cost = cost
		self.subscription_type = subscription_type
		self.is_activate = False
		self.is_paid = False
		
	def calculate_expiration_date(self):
		current_date = datetime.now()
		if self.subscription_type == 'monthly':
			return current_date + relativedelta(months=1)
		else:
			return current_date + relativedelta(years=1)

