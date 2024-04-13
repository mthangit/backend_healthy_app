from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail



db = SQLAlchemy()
masrhmallow = Marshmallow()
jwt = JWTManager()
bcrypt = Bcrypt()
mail = Mail()
