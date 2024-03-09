	new_book = Book(title, auth, year)
	db.session.add(new_book)
	db.session.commit()
