from flask import jsonify, request, Blueprint, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.subscription_services import add_subscription_services, get_subscription_by_user_id_services, user_has_subscription_services, update_subscription_services
import time
import urllib.parse
import hashlib
import requests
import json
import hmac
import uuid

subscriptions = Blueprint('subscriptions', __name__)

partner_code = 'MOMOBKUN20180529'
access_key = 'klm05TvNBzhg7h7j'
secret_key = 'at67qH6mk8w5Y1nAyMoYKMWACiEi2bsa';

# partner_code = "MOMO"
# access_key = "F8BBA842ECF85"
# secret_key = "K951B6PE1waDMi640xX08PD3vg6EkVlz"


endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
redirect_url = "https://premium-singularly-meerkat.ngrok-free.app/confirm_payment"  # Địa chỉ này phải thay đổi theo backend URL của bạn
ipn_url = "https://premium-singularly-meerkat.ngrok-free.app/ipn_momo"  # Địa chỉ này phải thay đổi theo backend URL của bạn
extraData = ""  

# @subscriptions.route('/api/create_payment_url', methods=['POST'])
# @jwt_required()
# def create_order():
#     user = get_jwt_identity()
#     user_id = user['account_id']
#     type = request.json.get('subscription_type')
#     if (type == 'monthly'):
#         cost = 50000
#     elif (type == 'yearly'):
#         cost = 550000
#     subscription_id = str(uuid.uuid4())
#     order = add_subscription_services(user_id, subscription_id, cost, type)
#     # convert order to json
#     order = json.loads(json.dumps(order))
#     if (order):
#         result = create_payment_url(type, order)
#         print(result)
#         return result
#     else:
#         return jsonify({'message': 'Error creating order'}), 400


@subscriptions.route('/api/create_payment_url', methods=['POST'])
@jwt_required()
def create_payment_url():
    user = get_jwt_identity()
    user_id = user['account_id']
    type = request.json.get('subscription_type')
    if (type == 'monthly'):
        cost = 50000
    elif (type == 'yearly'):
        cost = 550000
    subscription_id = str(uuid.uuid4())
    order = add_subscription_services(user_id, subscription_id, cost, type)
    
    amount = str(cost)
    order_id = subscription_id
    orderInfo = "Thanh toan Premium"
    request_id = str(uuid.uuid4())
    request_type = "payWithMethod"
    partnerName = "MoMo Payment"
    requestType = "payWithMethod"
    storeId = "Test Store"
    orderGroupId = ""
    autoCapture = True
    lang = "vi"
    orderGroupId = ""
    rawSignature = "accessKey=" + access_key + "&amount=" + amount + "&extraData=" + extraData + "&ipnUrl=" + ipn_url + "&orderId=" + order_id \
               + "&orderInfo=" + orderInfo + "&partnerCode=" + partner_code + "&redirectUrl=" + redirect_url\
               + "&requestId=" + request_id + "&requestType=" + requestType

    # rawSignature = "accessKey=" + access_key + "&amount=" + amount + "&extraData=" + extraData + "&ipnUrl=" + ipn_url + "&orderId=" + order_id + "&orderInfo=" + orderInfo + "&partnerCode=" + partner_code + "&redirectUrl=" + redirect_url + "&requestId=" + request_id + "&requestType=" + request_type
    h = hmac.new(bytes(secret_key, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()
    data = {
		'partnerCode': partner_code,
		'partnerName': "Test",
		'storeId': storeId,
		'requestId': request_id,
		'amount': amount,
		'orderId': order_id,
		'orderInfo': orderInfo,
		'redirectUrl': redirect_url,
		'ipnUrl': ipn_url,
		'lang': lang,
		'extraData': extraData,
		'requestType': request_type,
		'signature': signature,
        'orderGroupId': orderGroupId,
        'autoCapture': autoCapture
        
	}
    data = json.dumps(data)
    clen = len(data)
    response = requests.post(endpoint, data=data, headers={'Content-Type': 'application/json', 'Content-Length': str(clen)})
    result = response.json()
    return jsonify(result)
    # if result.get('errorCode') == 0:
    #     pay_url = result.get('payUrl')
    #     return jsonify({'payUrl': pay_url}), 200
    # else:
    #     return jsonify({'message': 'Error creating payment URL', 'errorCode': result.get('errorCode')}), 400

@subscriptions.route('/confirm_payment', methods=['GET', 'POST'])
def confirm_payment():
    # Logica để xác thực và xử lý phản hồi từ MoMo
    result_code = request.args.get('resultCode')
    if result_code == '0':
		# Thanh toán thành công
        return jsonify({'message': 'Payment confirmed'})


@subscriptions.route('/ipn_momo', methods=['POST'])
def ipn_momo():
    data = request.json
    code = data['resultCode']
    if(code == 0):
        return 204
    return jsonify({
        "Payment Failed"
	}), 400