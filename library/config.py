from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('KEY')
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/healthyapp"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')