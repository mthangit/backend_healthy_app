from .extension import masrhmallow

class UserSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'username', 'age', 'height', 'weight', 'gender', 'exercise', 'aim', 'is_deleted', 'account_id')

class AccountSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'email', 'password', 'created_at', 'authenticated')

class StatisticSchema(masrhmallow.Schema):
    class Meta:
        fields = ('user_id', 'date', 'morning_calo', 'noon_calo', 'dinner_calo', 'snack_calo', 'exercise_calo', 'water')