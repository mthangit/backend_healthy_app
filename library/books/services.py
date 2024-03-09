from ..extension import db
from ..library_ma import BookSchema
from ..model import Book
from flask import request

book_schema = BookSchema()
books_schema = BookSchema(many=True)

def add_book_service():
	book = request.get_json()

	# Validate the request
	if book and ('author' in book) and ('title' in book) and ('year' in book):
		auth = book['author']
		title = book['title']
		year = book['year']
		try :
			book = Book(title, auth, year)
			db.session.add(book)
			db.session.commit()
			return "Book added successfully"
		except IndentationError as e:
			db.session.rollback()
			return "Error adding book! Error details: " + str(e)
	else:
		return "Invalid request! Please provide author, title and year of the book"


def get_book_by_id_service(id):
	book = Book.query.get(id)
	if book:
		return book_schema.jsonify(book)
	else:
		return "Book not found!"
	
def get_all_book_service():
	books = Book.query.all()
	if books and len(books) > 0:
		return books_schema.jsonify(books)
	else:
		return "No books found!"