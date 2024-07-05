from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ultralytics import YOLO
from collections import Counter
from ..services.dish_services import get_recommend_dish_by_name
import cv2
import numpy as np
import time
import cloudinary
from datetime import datetime
import cloudinary.uploader
from ..config import (CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, CLOUDINARY_NAME)

detect = Blueprint('detect', __name__)

cloudinary.config( 
    cloud_name = CLOUDINARY_NAME,
    api_key = CLOUDINARY_API_KEY, 
    api_secret = CLOUDINARY_API_SECRET,
    secure=True
)

path = 'library/detect/best.pt'

@detect.route('/api/detect', methods=['POST'])
def get_class():
    try:
        file = request.files['image']
        print("Loading model")
        model = YOLO(path)
        print("Detecting")
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        results = model.predict(img)
        object_counts = []
        for result in results:
            names = result.names
            counts = Counter(result.boxes.cls.tolist())
            print(counts.items())
            for class_id, count in counts.items():
                object_counts.append(names[class_id])
        print(object_counts[0])
        if (object_counts[0] == 'ca'):
              recommend_dish = get_recommend_dish_by_name('Cá')
        else:
              recommend_dish = get_recommend_dish_by_name('Bò')
        return jsonify({
            "objects": object_counts,
            "recommend_dish": recommend_dish,
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Error"
        }), 500