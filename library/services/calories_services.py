from ..extension import db
from ..models.statistic import Statistic
from ..models.account import Account
from datetime import datetime

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

def get_user_calories_data(user_id):
    try:
        calories_data = Statistic.query.filter_by(user_id=user_id).first()
        if calories_data:
            return {
                'user_id': calories_data.user_id,
                'morning_calo': calories_data.morning_calo,
                'noon_calo': calories_data.noon_calo,
                'dinner_calo': calories_data.dinner_calo,
                'snack_calo': calories_data.snack_calo,
                'exercise_calo': calories_data.exercise_calo,
            }
        else:
            return None
    except Exception as e:
        print(str(e))
        return None
