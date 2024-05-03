from ..extension import db
from ..models.statistic import Statistic

def save_water_data(user_id, water):
    try:
        # Kiểm tra xem liệu dữ liệu water cho user đã tồn tại chưa
        existing_data = Statistic.query.filter_by(user_id=user_id).first()
        if existing_data:
            existing_data.water = water
        else:
            new_data = Statistic(
                user_id=user_id,
                water=water,
            )
            db.session.add(new_data)
        
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
