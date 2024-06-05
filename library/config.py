from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_ENGINE_OPTIONS = {
# 	'connect_args': {
# 		'ssl': {
# 			'ca': os.getenv('CA_CERT'),
# 		}
# 	}
# }


JWT_PRIVATE_KEY = os.getenv('JWT_PRIVATE_KEY')
JWT_PUBLIC_KEY = os.getenv('JWT_PUBLIC_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
FERNET_KEY = os.getenv('FERNET_KEY')

# MAIL_SERVER = 'smtp-legacy.office365.com'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
VNP_HASH_SECRET = os.getenv('VNP_HASHSECRET')
VNP_TMN_CODE = os.getenv('VNP_TMNCODE')
VNP_RETURN_URL = os.getenv('VNP_RETURN_URL')
VNP_ENDPOINT = os.getenv('VNP_ENDPOINT')
MOMO_ENDPOINT = os.getenv('MOMO_ENDPOINT')
MOMO_RETURN_URL = os.getenv('MOMO_RETURN_URL')
MOMO_IPN_URL = os.getenv('MOMO_IPN_URL')
MOMO_PARTNER_CODE = os.getenv('MOMO_PARTNER_CODE')
MOMO_ACCESS_KEY = os.getenv('MOMO_ACCESS_KEY')
MOMO_SECRET_KEY = os.getenv('MOMO_SECRET_KEY')