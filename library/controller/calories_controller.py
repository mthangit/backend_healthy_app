from flask import jsonify, request, Blueprint
from ..services.calories_services import save_calories_data

calories = Blueprint('calories', __name__)

@calories.route('/api/save-calories', methods=['POST'])
def save_calories():
    data = request.json
    morning_calo = data.get('morning_calo')
    noon_calo = data.get('noon_calo')
    dinner_calo = data.get('dinner_calo')
    snack_calo = data.get('snack_calo')
    exercise_calo = data.get('exercise_calo')
    water = data.get('water')
    success = save_calories_data(morning_calo, noon_calo, dinner_calo, snack_calo, exercise_calo, water)
    if success:
        return jsonify({'message': 'Calories data saved successfully'}), 200
    else:
        return jsonify({'message': 'Failed to save calories data'}), 500