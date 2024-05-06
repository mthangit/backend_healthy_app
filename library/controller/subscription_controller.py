from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

subscriptions = Blueprint('subscriptions', __name__)	
