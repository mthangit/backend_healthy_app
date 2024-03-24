from flask_mail import Message
from flask import render_template
from ..extension import mail
import time
def send_mail(subject, recipients, otp, username):
	current_time = time.localtime()
	current_date = time.strftime('%d %b, %Y', current_time)
	data = {
		'datetime': current_date,
		'otp': otp,
		'name': username
	}
	html = render_template('mail.html', data=data)
	msg = Message(subject=subject, sender=("Health Buddy", "21521428@gm.uit.edu.vn"), recipients=recipients)
	msg.html = html
	mail.send(msg)
	return True



