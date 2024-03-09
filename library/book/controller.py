from flask import jsonify, request, Blueprint
from .services import add_book_service, get_book_by_id_service, get_all_book_service


books = Blueprint('books', __name__)

@books.route('/add_book', methods=['POST'])
def add_book():
	return add_book_service()

@books.route('/book/<id>', methods=['GET'])
def get_book_by_id(id):
	return get_book_by_id_service(id)

@books.route('/all-books', methods=['GET'])
def get_books():
	return get_all_book_service()