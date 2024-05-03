from ..extension import db
from ..models.statistic import Statistic

def save_calories_data(user_id, morning_calo, noon_calo, dinner_calo, snack_calo, exercise_calo):
    try:
        # Kiểm tra xem liệu dữ liệu calo cho user đã tồn tại chưa
        existing_data = Statistic.query.filter_by(user_id=user_id).first()
        if existing_data:
            existing_data.morning_calo = morning_calo
            existing_data.noon_calo = noon_calo
            existing_data.dinner_calo = dinner_calo
            existing_data.snack_calo = snack_calo
            existing_data.exercise_calo = exercise_calo
        else:
            new_data = Statistic(
                user_id=user_id,
                morning_calo=morning_calo,
                noon_calo=noon_calo,
                dinner_calo=dinner_calo,
                snack_calo=snack_calo,
                exercise_calo=exercise_calo,
            )
            db.session.add(new_data)
        
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
