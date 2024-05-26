from datetime import datetime
from ..extension import db
from ..library_ma import SubscriptionSchema
# from ..model import User
from ..models.subscription import Subscription
from dateutil.relativedelta import relativedelta

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

def get_subscription_by_user_id_services(user_id):
	subscription = Subscription.query.filter_by(user_id=user_id).first()
	if subscription is None:
		return None
	return (subscription_schema.dump(subscription))

def check_subscription_services(user_id):
	subscription = Subscription.query.filter_by(user_id=user_id).all()
	if subscription is None:
		return False
	else:
		for sub in subscription:
			if sub.is_activate == 1 and sub.is_paid == 1:
				return True
		return False

def user_has_subscription_services(user_id):
	subscription = Subscription.query.filter_by(user_id=user_id).all()
	if subscription is None:
		return False
	else:
		for sub in subscription:
			if sub.is_activate == 1 and sub.is_paid == 1:
				return subscription_schema.dump(sub)
		return False

def add_subscription_services(user_id, subscription_id,  cost, subscription_type):
	subscription = Subscription(user_id, subscription_id, cost, subscription_type)
	db.session.add(subscription)
	db.session.commit()
	return subscription_schema.dump(subscription)

def update_subscription_services(subscription_id):
	# check the start_date and today, if today == start_date and not paid, then update the subscription
	subscription = Subscription.query.filter_by(subscription_id = subscription_id).first()
	subscription.is_activate = True
	subscription.is_paid = True
	subscription.payment_date = datetime.now()
	subscription.start_date = datetime.now()
	subscription.expired_date = subscription.calculate_expiration_date() + relativedelta(days=1)
	db.session.commit()
	return subscription_schema.dump(subscription)
