from library import create_app
from cryptography.fernet import Fernet
# from .library.config import FERNET_KEY
import time, asyncio
import base64
# from .library.utils.import_data import init_ingredient_data, init_dish_data, init_recipe_data


app = create_app()

# init_ingredient_data()

@app.route('/', methods=['GET'])	
def index():
	# return to a html page Hello World
	return "Hello World!"

if __name__ == '__main__':
	app.run(debug=True)
	# 121b81dc55849fc9f81a5f7dabe42b25680fc0afdb1a4e2134ce52c935595d4c


#ngrok http --domain=premium-singularly-meerkat.ngrok-free.app 5000