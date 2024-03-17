from library import create_app

app = create_app()

@app.route('/')
def homepage():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)