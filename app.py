from library import create_app
from cryptography.fernet import Fernet
import time, asyncio
import base64


app = create_app()


@app.route('/', methods=['GET'])	
def index():
	# return to a html page Hello World
	return "Hello World!"

if __name__ == '__main__':
	app.run(debug=True)
	
	# 121b81dc55849fc9f81a5f7dabe42b25680fc0afdb1a4e2134ce52c935595d4c


#ngrok http --domain=premium-singularly-meerkat.ngrok-free.app 5000