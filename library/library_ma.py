from .extension import masrhmallow

class UserSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'username', 'age', 'height', 'weight', 'gender', 'exercise', 'aim', 'is_deleted', 'account_id')

class AccountSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'email', 'password', 'created_at', 'authenticated')

class IngredientSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'name', 'calo', 'carb', 'fat', 'protein', 'canxi' , 'img', 'category')

class DishSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'name', 'calo', 'carb', 'fat', 'protein', 'img','is_premium', 'main_category')

class RecipeSchema(masrhmallow.Schema):
	class Meta:
		fields = ('ingredient_id', 'dish_id', 'unit', 'grams')

class MenuSchema(masrhmallow.Schema):
	class Meta:
		fields = ('id', 'name')
	
class CannotEatSchema(masrhmallow.Schema):
	class Meta:
		fields = ('disease_id', 'ingredient_id')

class FavoriteSchema(masrhmallow.Schema):
	class Meta:
		fields = ('user_id', 'dish_id', 'value')
class StatisticSchema(masrhmallow.Schema):
    class Meta:
        fields = ('user_id', 'date', 'morning_calo', 'noon_calo', 'dinner_calo', 'snack_calo', 'exercise_calo', 'water')
class SubscriptionSchema(masrhmallow.Schema):
	class Meta:
		fields = ('user_id', 'subscription_id' ,'is_activate', 'start_date', 'is_paid', 'cost', 'payment_date', 'subscription_type', 'expired_date', 'created_date')
