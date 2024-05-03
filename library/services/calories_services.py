from ..extension import db
from ..model import Statistic
from flask_jwt_extended import get_jwt_identity
from datetime import datetime

def save_calories_data(morning_calo, noon_calo, dinner_calo, snack_calo, exercise_calo, water):
    try:
        user_id = get_jwt_identity().get('user_id')
        new_statistic = Statistic(
            user_id=user_id,
            date=datetime.now().date(),
            morning_calo=morning_calo,
            noon_calo=noon_calo,
            dinner_calo=dinner_calo,
            snack_calo=snack_calo,
            exercise_calo=exercise_calo,
            water=water
        )
        db.session.add(new_statistic)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False