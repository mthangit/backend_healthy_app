# from ..model.ingredient import Ingredient
# from ..model.dish import Dish
from ..models.ingredient import Ingredient
from ..models.dish import Dish
from ..models.recipe import Recipe
from ..extension import db
import pandas as pd
from flask import jsonify, request, Blueprint

data = Blueprint('data', __name__)


@data.route('/api/init-data', methods=['GET'])
def init_data():
	# init_ingredient_data()
	# init_dish_data()
	init_recipe_data()
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
    df = pd.read_csv('dish.csv')
    for index, row in df.iterrows():
        dish = Dish(
            name=row[0],
            main_category=row[1]
        )
        db.session.add(dish)
    db.session.commit()

def init_recipe_data():
    print('Initializing recipe data')
    df = pd.read_csv('recipe.csv')
    for index, row in df.iterrows():
        recipe = Recipe(
            ingredient_id=row[0],
            dish_id=row[1],
            grams=row[2]
        )
        db.session.add(recipe)
    db.session.commit()

