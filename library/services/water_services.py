from ..extension import db
from ..models.statistic import Statistic
from ..models.account import Account

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

def get_user_water_data(user_id):
    try:
        calories_data = Statistic.query.filter_by(user_id=user_id).first()
        if calories_data:
            return {
                'user_id': calories_data.user_id,
                'water': calories_data.water,
            }
        else:
            return None
    except Exception as e:
        print(str(e))
        return None
