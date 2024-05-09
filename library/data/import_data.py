# from ..model.ingredient import Ingredient
# from ..model.dish import Dish
from ..models.ingredient import Ingredient
from ..models.dish import Dish
from ..models.recipe import Recipe
from ..models.disease import Disease
from ..models.cannot_eat import CannotEat
from ..models.user import User
from ..models.favorite import Favorite
from ..extension import db
import pandas as pd
from flask import jsonify, request, Blueprint

data = Blueprint('data', __name__)


@data.route('/api/init-data', methods=['GET'])
def init_data():
	init_favorite_data()
	# init_ingredient_data()
	# init_dish_data()
	# update_dish_data()
	# init_recipe_data()
	return jsonify({'message': 'Data initialized'}), 200

@data.route('/api/update-ingredient', methods=['GET'])
def update_ingredient():
	update_canxi_ingredient()
	return jsonify({'message': 'Update ingredient successfully'}), 200

@data.route('/api/update-recipe', methods=['GET'])
def update_recipe():
	recipes = Recipe.query.all()
	for recipe in recipes:
		recipe.grams = recipe.calculate_grams()
	db.session.commit()
	return jsonify({'message': 'Update recipe successfully'}), 200


def init_ingredient_data():
    print('Initializing ingredient data')
    df = pd.read_csv('ingredient.csv')
    for index, row in df.iterrows():
        ingredient = Ingredient(
            name=row[0],
            calo=row[2],
            carb=row[5],
            fat=row[4],
            protein=row[3],
            category=row[15]
        )
        db.session.add(ingredient)
    db.session.commit()
    
def update_canxi_ingredient():
    df = pd.read_csv('ingredient.csv')
    for index, row in df.iterrows():
        ingredient = Ingredient.query.filter_by(name=row[0]).first()
        if ingredient:
              ingredient.canxi = row[6]
    db.session.commit()



def init_dish_data():
	print('Initializing dish data')
	df = pd.read_csv('dish_data.csv')
	for index, row in df.iterrows():
		dish = Dish(
			name=row[0],
			main_category=row[1]
		)
		dish_existed = Dish.query.filter_by(name=row[0]).first()
		if not dish_existed:
			db.session.add(dish)
	db.session.commit()

def init_recipe_data():
	print('Initializing recipe data')
	df = pd.read_csv('recipe_data.csv')
	for index, row in df.iterrows():
		recipe = Recipe(
			ingredient_id=row[0],
			dish_id=row[1],
			unit=row[2]
		)
		# recipe_existed = Recipe.query.filter_by(ingredient_id=row[0], dish_id=row[1]).first()\
		# # recipre existed with ingredient_id or dish_id
		# if not recipe_existed:
		# 	db.session.add(recipe)
		# else:
		# 	recipe_existed.unit = row[2]
		db.session.add(recipe)
	db.session.commit()


def init_disease_data():
	print('Initializing disease data')
	df = pd.read_csv('disease.csv')
	for index, row in df.iterrows():
		disease = Disease(
			name=row[0],
			description=row[1]
		)
		db.session.add(disease)
	db.session.commit()
      
def init_cannot_eat_data():
	print('Initializing cannot eat data')
	df = pd.read_csv('cannot_eat_data.csv')
	for index, row in df.iterrows():
		cannot_eat = CannotEat(
			disease_id=row[0],
			ingredient_id=row[1]
		)
		db.session.add(cannot_eat)
	db.session.commit()


def update_dish_data():
	print('Updating dish data')
	dishes = Dish.query.all()
	for dish in dishes:
		nutrition = dish.to_dict()
		print(nutrition)
		dish.calo = nutrition.get('calo')
		dish.protein = nutrition.get('protein')
		dish.carb = nutrition.get('carb')
		dish.fat = nutrition.get('fat')
		dish.canxi = nutrition.get('canxi')
	db.session.commit()


def init_user_data():
	print('Initializing user data')
	df = pd.read_csv('user_data.csv')
	for index, row in df.iterrows():
		user = User(
			username=row[0],
			age=row[1],
			height=row[2],
			weight=row[3],
			gender=row[4],
			exercise=row[5],
			aim=row[6],
			disease_id=row[7]
		)
		db.session.add(user)
	db.session.commit()

def init_favorite_data():
	print('Initializing favorite data')
	df = pd.read_csv('favorite_data_unique.csv')
	for index, row in df.iterrows():
		favorite = Favorite(
			user_id=row[0],
			dish_id=row[1]
		)
		db.session.add(favorite)
	db.session.commit()