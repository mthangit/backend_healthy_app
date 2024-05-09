from ..extension import db
from ..models.statistic import Statistic
from ..models.account import Account
from datetime import datetime
from flask import Blueprint, jsonify, request

def save_calories_morning(user_id,morning_calo):
    try: 
        user_account = Account.query.filter_by(id = user_id).first()
        if user_account:
            new_morning_calo = morning_calo
            new_statistic = Statistic(user_id = user_id)
            new_statistic.morning_calo = new_morning_calo
            db.session.add(new_statistic)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return False

def save_calories_noon(user_id,noon_calo):
    try: 
        user_account = Account.query.filter_by(id = user_id).first()
        if user_account:
            new_noon_calo = noon_calo
            new_statistic = Statistic(user_id = user_id)
            new_statistic.noon_calo = new_noon_calo
            db.session.add(new_statistic)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return False

def save_calories_dinner(user_id,dinner_calo):
    try: 
        user_account = Account.query.filter_by(id = user_id).first()
        if user_account:
            new_dinner_calo = dinner_calo
            new_statistic = Statistic(user_id = user_id)
            new_statistic.dinner_calo = new_dinner_calo
            db.session.add(new_statistic)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return False
    
def save_calories_snack(user_id,snack_calo):
    try: 
        user_account = Account.query.filter_by(id = user_id).first()
        if user_account:
            new_snack_calo = snack_calo
            new_statistic = Statistic(user_id = user_id)
            new_statistic.snack_calo = new_snack_calo
            db.session.add(new_statistic)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return False
    
def save_calories_exercise(user_id,exercise_calo):
    try: 
        user_account = Account.query.filter_by(id = user_id).first()
        if user_account:
            new_exercise_calo = exercise_calo
            new_statistic = Statistic(user_id = user_id)
            new_statistic.exercise_calo = new_exercise_calo
            db.session.add(new_statistic)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return False

def get_user_calories_data(user_id):
    try:
        calories_data = Statistic.query.filter_by(user_id=user_id).first()
        if calories_data:
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
                    "total_morning_calo": 0,
                    "total_noon_calo": 0,
                    "total_dinner_calo": 0,
                    "total_snack_calo": 0,
                    "total_exercise_calo": 0
                }), 200
            results = {
                "user_id": user_id,
                "date": current_date.strftime("%d-%m-%Y"),
                "total_morning_calo": sum([item.morning_calo for item in user_statistic]),
                "total_noon_calo": sum([item.noon_calo for item in user_statistic]),
                "total_dinner_calo": sum([item.dinner_calo for item in user_statistic]),
                "total_snack_calo": sum([item.snack_calo for item in user_statistic]),
                "total_exercise_calo": sum([item.exercise_calo for item in user_statistic])
            }
            # print(results)
            return results
        else:
            return jsonify({'message': 'No data found'}), 404
    except Exception as e:
        print(str(e))
        return jsonify({'message': str(e)}), 500
