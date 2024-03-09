from library import create_app

app = create_app()

@app.route('/')
def homepage():
	return 'Hello, World!'

@app.route('/about', methods=['GET'])
def about():
	return 'The about page' 

if __name__ == '__main__':
	app.run(debug=True)