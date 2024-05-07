from ..extension import db
from ..library_ma import SubscriptionSchema
# from ..model import User
from ..models.subscription import Subscription

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

def get_subscription_by_user_id_services(user_id):
	subscription = Subscription.query.filter_by(user_id=user_id).first()
	if subscription is None:
		return None
	return (subscription_schema.dump(subscription))


def user_has_subscription_services(user_id):
	subscription = Subscription.query.filter_by(user_id=user_id).first()
	if subscription is None:
		return False
	return True