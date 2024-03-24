from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
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
