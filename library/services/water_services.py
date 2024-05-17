from ..extension import db
from ..models.statistic import Statistic
from ..models.account import Account
from datetime import datetime
from flask import Blueprint, jsonify, request

def save_water(user_id,water):
    try: 
        user_account = Account.query.filter_by(id = user_id).first()
        if user_account:
            new_water = water
            new_statistic = Statistic(user_id = user_id)
            new_statistic.water = new_water
            db.session.add(new_statistic)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return False

# def get_user_water_data(user_id):
#     try:
#         calories_data = Statistic.query.filter_by(user_id=user_id).first()
#         if calories_data:
#             return {
#                 'user_id': calories_data.user_id,
#                 'water': calories_data.water,
#             }
#         else:
#             return None
#     except Exception as e:
#         print(str(e))
#         return None

def get_user_water_data(user_id):
    try:
        water_data = Statistic.query.filter_by(user_id=user_id).first()
        if water_data:
            current_date = datetime.now().date()
            day, month, year = current_date.day, current_date.month, current_date.year
            user_statistic = Statistic.query.filter(
                Statistic.user_id == user_id,
                db.extract('day', Statistic.date) == day,
                db.extract('month', Statistic.date) == month,
                db.extract('year', Statistic.date) == year
            ).all()
            if not user_statistic:
                return jsonify({
                    "user_id": user_id,
                    "date": current_date.strftime("%d-%m-%Y"), 
                    "total_water": 0,
                }), 200
            results = {
                "user_id": user_id,
                "date": current_date.strftime("%d-%m-%Y"),
                "total_water": sum([item.water for item in user_statistic]),
            }
            # print(results)
            return results
        else:
            return jsonify({'message': 'No data found'}), 404
    except Exception as e:
        print(str(e))
        return jsonify({'message': str(e)}), 500