from ..extension import db
from flask import jsonify
from sqlalchemy import ForeignKey
from .ingredient import Ingredient


class Recipe(db.Model):
    ingredient_id = db.Column(db.Integer, ForeignKey('ingredient.id'), primary_key=True)
    dish_id = db.Column(db.Integer, ForeignKey('dish.id'), primary_key=True)
    unit = db.Column(db.Float)

    def __init__(self, ingredient_id, dish_id, unit):
        self.ingredient_id = ingredient_id
        self.dish_id = dish_id
        self.unit = unit

    def __repr__(self):
        return f'<Recipe {self.ingredient_id} {self.dish_id}>'
    
    def get_unit(self):
        return self.unit
    
    def calculate_grams(self):
        detail_ingr = Ingredient.query.filter_by(id=self.ingredient_id).first()
        if detail_ingr.category == 'Grains':
            return 100*self.unit*20/detail_ingr.carb
        elif detail_ingr.category == 'Vegetables' or detail_ingr.category == 'Fruits':
            return 80*self.unit
        elif detail_ingr.category == 'Protein':
            return 100*self.unit*7/detail_ingr.protein
        elif detail_ingr.category == 'Dairy':
            return 100*self.unit*100/detail_ingr.canxi
        elif detail_ingr.category == 'Fats and oils':
            return 100*self.unit*5/detail_ingr.fat
        elif detail_ingr.category == 'Sugar':
            return 5*self.unit
        elif detail_ingr.category == 'Salt and sauces':
            return 1*self.unit
        else:
            return 0
    
    def get_recipe_detail(self):
        grams = self.calculate_grams()
        detail_ingr = Ingredient.query.filter_by(id=self.ingredient_id).first()
        if detail_ingr:
            recipe_details = {
                'ingredient_id': self.ingredient_id,
                'name': detail_ingr.name,
                'unit': self.unit,
                'grams': round(grams, 2),
                'calo': round(grams*detail_ingr.calo/100, 2),
                'protein': round(grams*detail_ingr.protein/100, 2),
                'fat': round(grams*detail_ingr.fat/100, 2),
                'carb': round(grams*detail_ingr.carb/100, 2),
                'canxi': round(grams*detail_ingr.canxi/100, 2),
                'category': detail_ingr.category
            }
            return recipe_details
        else:
            return jsonify({'message': 'Ingredient not found'}), 404

    