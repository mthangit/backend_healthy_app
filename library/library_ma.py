from .extension import masrhmallow

class UserSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'username', 'age', 'height', 'weight', 'gender', 'excersise', 'aim', 'is_deleted')

class AccountSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'user_id', 'email', 'password', 'created_at')