from ..model import Ingredient, Dish, Recipe
from ..extension import db
import pandas as pd
from flask import jsonify, request, Blueprint

data = Blueprint('data', __name__)


@data.route('/api/init-data', methods=['GET'])
def init_data():
	# init_ingredient_data()
	init_dish_data()
	init_recipe_data()
	return jsonify({'message': 'Data initialized'}), 200


def init_ingredient_data():
    print('Initializing ingredient data')
    df = pd.read_csv('ingredient.csv')
    for index, row in df.iterrows():
        ingredient = Ingredient(
            # name=row[0],
            # removal=row[1],
            # kcal=row[2],
            # protein=row[3],
            # lipid=row[4],
            # glucid=row[5],
            # canxi=row[6],
            # phosphor=row[7],
            # fe=row[8],
            # vitamin_a=row[9],
            # beta_caroten=row[10],
            # vitamin_b1=row[11],
            # vitamin_b2=row[12],
            # vitamin_pp=row[13],
            # vitamin_c=row[14],
            # category=row[15]
            name=row[0],
            calo=row[2],
            carb=row[5],
            fat=row[4],
            protein=row[3]
        )
        db.session.add(ingredient)
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
    df = pd.read_csv('recipe_data.csv')
    for index, row in df.iterrows():
        recipe = Recipe(
            ingredient_id=row[0],
            dish_id=row[1],
            unit=row[2]
        )
        db.session.add(recipe)
