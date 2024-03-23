from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')