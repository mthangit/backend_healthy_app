from ..extension import db
from ..library_ma import RecipeSchema
from ..models.recipe import Recipe
from ..models.ingredient import Ingredient
from ..models.dish import Dish
from flask import request, jsonify
from ..genetic_algorithm.genetic_algorithm import GeneticAlgorithm


def get_menu(account_id):
    GA = GeneticAlgorithm(10, 0.1, 10, account_id)
    a = GA.main_genetic_algorithm()
    if a: 
        return a
 
