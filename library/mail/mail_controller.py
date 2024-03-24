from flask import jsonify, request, Blueprint
from .mail_services import send_mail
mail = Blueprint('mail', __name__)

@mail.route('/api/send-mail', methods=['POST'])
def send_mail_route():
	# subject = request.json.get('subject')
	# sender = request.json.get('sender')
	# recipients = request.json.get('recipients')
	# body = request.json.get('body')
	send_mail("Activate your HealthBuddy account",["21521505@gm.uit.edu.vn", "21520429@gm.uit.edu.vn", "21522438@gm.uit.edu.vn", "21521936@gm.uit.edu.vn", "21521428@gm.uit.edu.vn"], "123456", "Team rén thầy Thuân")
	return jsonify({'message': 'Mail sent successfully'}), 200