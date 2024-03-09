from flask import Flask, jsonify, request, Blueprint
from dotenv import load_dotenv
from .extension import db, masrhmallow
from .model import Book
from .book.controller import books
import os


def create_app(config_file = 'config.py'):
	app = Flask(__name__)
	app.config.from_pyfile(config_file)

	db.init_app(app)
	masrhmallow.init_app(app)
	with app.app_context():
		db.create_all()
		print('Database created!')
	app.register_blueprint(books)
	return app