from .extension import masrhmallow

class UserSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'username', 'age', 'height', 'weight', 'gender', 'exercise', 'aim', 'is_deleted', 'account_id')

class AccountSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'email', 'password', 'created_at', 'authenticated')

class IngredientSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'name', 'calo', 'carb', 'fat', 'protein', 'img')

class DishSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'name', 'calo', 'carb', 'fat', 'protein', 'img')

