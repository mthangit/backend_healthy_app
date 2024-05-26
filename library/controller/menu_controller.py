from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from ..services.menu_services import get_menu
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.suggested_menu import SuggestedMenu
from ..models.account import Account
from ..models.meal import Meal
from ..models.dish import Dish
from ..extension import db
from datetime import datetime
from sqlalchemy import func
from ..genetic_algorithm.genetic_algorithm import GeneticAlgorithm

menus = Blueprint('menus', __name__)

# @menus.route('/api/get-menu', methods=['GET'])
# @jwt_required()
# def get_menu_controller():
#     try:
#         account_id = get_jwt_identity()['account_id']
#         if not account_id:
#             return jsonify({'message': 'Account not found'}), 404
#         menu = get_menu(account_id)
#         if menu:
#             return jsonify(menu), 200
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500
@menus.route('/api/new_genetic_algorithm', methods=["GET"])
@jwt_required()
def new_genetic_algorithm():
    account_id = get_jwt_identity()['account_id']
    user_account = Account.query.filter_by(id = account_id).first()
    if not user_account:
        return jsonify({'message': 'Unauthorized'}), 404
    GA = GeneticAlgorithm(10, 0.2, 5, account_id)
    a = GA.main_genetic_algorithm()
    current_date = datetime.utcnow().date()
    max_num_suggest = (SuggestedMenu.query.with_entities(func.max(SuggestedMenu.num_suggest))
                       .filter(SuggestedMenu.user_id == account_id, 
                               db.func.date(SuggestedMenu.date_suggest) == current_date).scalar())
    if max_num_suggest:
        new_num_suggest = max_num_suggest + 1
    else:
        new_num_suggest = 1
    new_menu = SuggestedMenu(user_id= account_id , fitness_score=a['fitness'], 
                             num_suggest=new_num_suggest)
    db.session.add(new_menu)
    db.session.commit()
    for meal_data in a['data']:
        dish_id = meal_data['dish_id']
        dish_order = meal_data['dish_order']
        meal_type = meal_data['meal_type']
        meal = Meal(menu_id=new_menu.id, dish_order=dish_order, dish_id=dish_id, meal_type=meal_type)
        db.session.add(meal)
    db.session.commit()
    return a

@menus.route('/api/get-suggest-menu', methods=['GET'])
@jwt_required()
def get_suggest_menu():
        account_id = get_jwt_identity()['account_id']
        user_account = Account.query.filter_by(id = account_id).first()
        if not user_account:
            return jsonify({'message': 'Account not found'}), 404
        current_date = datetime.utcnow().date()
        max_suggest_subquery = (db.session.query(func.max(SuggestedMenu.num_suggest))
                            .filter(SuggestedMenu.user_id == user_account.id, 
                                    db.func.date(SuggestedMenu.date_suggest) == current_date).scalar())
        if max_suggest_subquery:
            result = (db.session.query(SuggestedMenu, Meal, Dish)
                .join(Meal, SuggestedMenu.id == Meal.menu_id)
                .join(Dish, Meal.dish_id == Dish.id)
                .filter(SuggestedMenu.user_id == account_id, 
                        db.func.date(SuggestedMenu.date_suggest) == current_date, 
                        SuggestedMenu.num_suggest == max_suggest_subquery).all())
            morning_dishs = []
            noon_dishs = []
            dinner_dishs = []
            snack_dishs = []
            total_kcal = 0
            for suggested_menu, meal, dish in result:
                if meal.meal_type == "morning":
                    total_kcal += dish.to_dict()['calo']
                    morning_dishs.append(dish.to_dict())
                elif meal.meal_type == "noon":
                    total_kcal += dish.to_dict()['calo']
                    noon_dishs.append(dish.to_dict())
                elif meal.meal_type == "evening":
                    total_kcal += dish.to_dict()['calo']
                    dinner_dishs.append(dish.to_dict())
                else: 
                    total_kcal += dish.to_dict()['calo']
                    snack_dishs.append(dish.to_dict())
            return jsonify({
            "morning_dishs": morning_dishs,
            "noon_dishs": noon_dishs,
            "dinner_dishs": dinner_dishs,
            "snacks": snack_dishs,
            "fitness_score": suggested_menu.fitness_score,
            "calo": round(total_kcal, 2)
            })
        else:
            return jsonify({
            "morning_dishs": [],
            "noon_dishs": [],
            "dinner_dishs": [],
            "snacks": [],
            "fitness_score": 0,
            "kcal": 0
        })