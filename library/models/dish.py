from ..extension import db
from flask import jsonify
from .recipe import Recipe
import random

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    calo = db.Column(db.Float, nullable=False)
    carb = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    canxi = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(255), nullable=False)
    is_premium = db.Column(db.Boolean, default=False)
    main_category = db.Column(db.String(255), nullable=False)

    def __init__(self, name, main_category):
        self.name = name
        self.main_category = main_category
 
    def __repr__(self):
        return f'<Dish {self.name}>'
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_main_category(self):
        return self.main_category
    
    def to_dict(self):
        recipes = Recipe.query.filter_by(dish_id=self.id).all()
        total_kcal = 0
        total_protein = 0
        total_lipid = 0
        total_glucid = 0
        total_canxi = 0
        if recipes:
            for recipe in recipes:
                ingredient_details = recipe.get_recipe_detail()
                total_kcal  += ingredient_details['calo']
                total_protein  += ingredient_details['protein']
                total_glucid  += ingredient_details['carb']
                total_lipid  += ingredient_details['fat']
                total_canxi  += ingredient_details['canxi']
                # total_phosphor += ingredient_details['phosphor']
                # total_fe += ingredient_details['fe']
                # total_vitamin_a += ingredient_details['vitamin_a']
                # total_beta_caroten += ingredient_details['beta_caroten']
                # total_vitamin_b1 += ingredient_details['vitamin_b1']
                # total_vitamin_b2 += ingredient_details['vitamin_b2']
                # total_vitamin_pp += ingredient_details['vitamin_pp']
                # total_vitamin_c += ingredient_details['vitamin_c']
                
            total_nutrition = {
                "id": self.id,
                "name": self.name,
                "main_category": self.main_category,
                "calo" : round(total_kcal, 2),
                "protein": round(total_protein, 2),
                "carb": round(total_glucid, 2),
                "fat": round(total_lipid, 2),
                "canxi": round(total_canxi, 2),
                # "phosphor": round(total_phosphor, 2),
                # "fe": round(total_fe, 2),
                # "vitamin_a": round(total_vitamin_a, 2),
                # "beta_caroten": round(total_beta_caroten, 2),
                # "vitamin_b1": round(total_vitamin_b1, 2),
                # "vitamin_b2": round(total_vitamin_b2, 2),
                # "vitamin_pp": round(total_vitamin_pp, 2),
                # "vitamin_c": round(total_vitamin_c, 2),
                }
            return total_nutrition
        else:
            return {
                "id": self.id,
                "name": self.name,
                "main_category": self.main_category,
                "total_kcal" : 0,
            }

