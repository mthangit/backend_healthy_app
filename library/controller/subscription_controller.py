from flask import jsonify, request, Blueprint, redirect, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.subscription_services import add_subscription_services, get_subscription_by_user_id_services, user_has_subscription_services, update_subscription_services
import time
import urllib.parse
import hashlib
import requests
import json
import hmac
import uuid
import random
from datetime import datetime

subscriptions = Blueprint('subscriptions', __name__)

# partner_code = 'MOMOBKUN20180529'
# access_key = 'klm05TvNBzhg7h7j'
# secret_key = 'at67qH6mk8w5Y1nAyMoYKMWACiEi2bsa';

partner_code = "MOMO"
access_key = "F8BBA842ECF85"
secret_key = "K951B6PE1waDMi640xX08PD3vg6EkVlz"


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


@subscriptions.route('/api/create_payment_url/momo', methods=['POST'])
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

def get_client_ip(request):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.remote_addr
    return ip

n = random.randint(10**11, 10**12 - 1)
n_str = str(n)
while len(n_str) < 12:
    n_str = '0' + n_str

def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()


@subscriptions.route('/api/get_ip', methods=['POST'])
def get_client_ip_adr():
    return jsonify({
        'ip': get_client_ip(request)
	})

vnp_HashSecret = "QY2QZDHB9AMF3IJJAKEASJD8ARLZM90B"
vnp_TmnCode = "COITO8B1"
vnp_Url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
vnp_ReturnUrl = "https://premium-singularly-meerkat.ngrok-free.app/confirm_payment/vnpay"
vnp_Version = "2.1.0"
vnp_CurrCode = "VND"
vnp_Command = "pay"
vnp_OrderType = "other"
vnp_Locale = "vn"


@subscriptions.route('/api/create_payment_url/vnpay', methods=['POST'])
@jwt_required()
def create_payment_vnpay():
    user = get_jwt_identity()
    user_id = user['account_id']
    type = request.json.get('subscription_type')
    if (type == 'monthly'):
        cost = 50000
    elif (type == 'yearly'):
        cost = 550000 
    vnp_Amount = cost * 100
    subscription_id = str(uuid.uuid4())
    order = add_subscription_services(user_id, subscription_id, cost, type)
    vnp_IpAddr = get_client_ip(request)
    vnp_OrderInfo = "Thanh toan Premium"
    vnp_TxnRef = subscription_id
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    inputData = {
        'vnp_Version': vnp_Version,
        'vnp_Command': vnp_Command,
        'vnp_TmnCode': vnp_TmnCode,
        'vnp_Amount': vnp_Amount,
        'vnp_CurrCode': vnp_CurrCode,
        'vnp_TxnRef': vnp_TxnRef,
        'vnp_OrderInfo': vnp_OrderInfo,
        'vnp_OrderType': vnp_OrderType,
        'vnp_Locale': vnp_Locale,
        'vnp_ReturnUrl': vnp_ReturnUrl,
        'vnp_IpAddr': vnp_IpAddr,
        'vnp_CreateDate': vnp_CreateDate
    }
    sortedData = sorted(inputData.items())
    
    # Build the query string
    queryString = '&'.join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sortedData])
    
    # Calculate the secure hash
    secureHash = hmacsha512(vnp_HashSecret, queryString)
    # Build the full URL
    vnp_PayUrl = f"{vnp_Url}?{queryString}&vnp_SecureHash={secureHash}"
    return jsonify({'url': vnp_PayUrl}), 200

@subscriptions.route('/confirm_payment/momo', methods=['GET', 'POST'])
def confirm_payment_momo():
    # Logica để xác thực và xử lý phản hồi từ MoMo
    result_code = request.args.get('resultCode')
    if result_code == '0':
		# Thanh toán thành công
        return jsonify({'message': 'Payment confirmed'})


@subscriptions.route('/confirm_payment/vnpay', methods=['GET', 'POST'])
def confirm_payment_vnpay():
    # Logica để xác thực và xử lý phản hồi từ MoMo
    responseCode = request.args.get('vnp_ResponseCode')
    transactionStatus = request.args.get('vnp_TransactionStatus')
    if responseCode == '00' and transactionStatus == '00':
		# Thanh toán thành công
        return jsonify({'message': 'Payment confirmed'})


@subscriptions.route('/ipn_momo', methods=['POST'])
def ipn_momo():
    data = request.json
    code = data['resultCode']
    orderId = data['orderId']
    if(code == 0):
        update_subscription_services(orderId)
        # RETURN CODE 204
        return Response(status=204)
    return jsonify({
        "Payment Failed"
	}), 400

def validateSignatureVNPAY(data):
    secret_key = vnp_HashSecret
    vnp_SecureHash = data.get('vnp_SecureHash')
    if vnp_SecureHash:
        del data['vnp_SecureHash']
    if 'vnp_SecureHashType' in data:
        del data['vnp_SecureHashType']
    inputData = sorted(data.items())
    hasData = ''
    seq = 0
    for key, val in inputData:
        if str(key).startswith('vnp_'):
            if seq == 1:
                hasData = hasData + "&" + str(key) + '=' + urllib.parse.quote_plus(str(val))
            else:
                seq = 1
                hasData = str(key) + '=' + urllib.parse.quote_plus(str(val))
    hashValue = hmacsha512(secret_key, hasData)
    print('Validate debug, HashData:' + hasData + "\n HashValue:" + hashValue + "\nInputHash:" + vnp_SecureHash)
    return vnp_SecureHash == hashValue


@subscriptions.route('/ipn_vnpay', methods=['GET'])
def ipn_vnpay():
	data = request.args.to_dict()
	if validateSignatureVNPAY(data):
		vnp_ResponseCode = request.args.get('vnp_ResponseCode')
		vnp_TransactionStatus = request.args.get('vnp_TransactionStatus')
		vnp_TxnRef = request.args.get('vnp_TxnRef')
		if vnp_ResponseCode == '00':
			if vnp_TransactionStatus == '00':
				update_subscription_services(vnp_TxnRef)
			return jsonify({'RspCode': '00', 'Message': 'Success'})
		else:
			return jsonify({'RspCode': '01', 'Message': 'Fail'})
	else:
		return jsonify({'RspCode': '97', 'Message': 'Invalid signature'})
		
	