from library import create_app
from cryptography.fernet import Fernet
# from .library.config import FERNET_KEY
import time, asyncio
import base64


app = create_app()

if __name__ == '__main__':
	(app.run(debug=True))
	# 121b81dc55849fc9f81a5f7dabe42b25680fc0afdb1a4e2134ce52c935595d4c
