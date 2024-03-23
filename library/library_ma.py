from .extension import masrhmallow

class UserSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'username', 'age', 'height', 'weight', 'gender', 'exercise', 'aim', 'is_deleted', 'account_id')

class AccountSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'email', 'password', 'created_at')