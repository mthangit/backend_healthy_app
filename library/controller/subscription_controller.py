from flask import jsonify, request, Blueprint, redirect, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.subscription_services import (
     										add_subscription_services, 
                                            get_subscription_by_user_id_services, 
                                            user_has_subscription_services, 
                                            update_subscription_services
                                            )
import time
import urllib.parse
import hashlib
import requests
import json
import hmac
import uuid
import random
from datetime import datetime, timedelta
from config import (
     				VNP_ENDPOINT,
     				VNP_HASH_SECRET, 
                    VNP_TMNCODE, 
                	VNP_RETURN_URL, 
                    MOMO_RETURN_URL, 
                    MOMO_IPN_URL, 
                    MOMO_ENDPOINT,
                    MOMO_ACCESS_KEY,
                    MOMO_PARTNER_CODE,
                    MOMO_SECRET_KEY
                )

subscriptions = Blueprint('subscriptions', __name__)


@subscriptions.route('/api/create_payment_url/momo', methods=['POST'])
@jwt_required()
def create_payment_url():
    user = get_jwt_identity()
    user_id = user['account_id']
    type = request.json.get('subscription_type')
    if (type == 'monthly'):
        cost = 50000
        loai = 'thang'
    elif (type == 'yearly'):
        cost = 550000
        loai = 'nam'
    subscription_id = str(uuid.uuid4())
    order = add_subscription_services(user_id, subscription_id, cost, type)
    
    amount = str(cost)
    order_id = subscription_id
    orderInfo = "Thanh toan Premium HealthyBuddy 1 " + loai
    request_id = str(uuid.uuid4())
    requestType = "payWithMethod"
    storeId = "Test Store"
    orderGroupId = ""
    autoCapture = True
    lang = "vi"
    orderGroupId = ""
    extraData = ""  
    rawSignature = "accessKey=" + MOMO_ACCESS_KEY + "&amount=" + amount + "&extraData=" + extraData + "&ipnUrl=" + MOMO_IPN_URL + "&orderId=" + order_id \
               + "&orderInfo=" + orderInfo + "&partnerCode=" + MOMO_PARTNER_CODE + "&redirectUrl=" + MOMO_RETURN_URL\
               + "&requestId=" + request_id + "&requestType=" + requestType

    h = hmac.new(bytes(MOMO_SECRET_KEY, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()
    data = {
		'partnerCode': MOMO_PARTNER_CODE,
		'partnerName': "Test",
		'storeId': storeId,
		'requestId': request_id,
		'amount': amount,
		'orderId': order_id,
		'orderInfo': orderInfo,
		'redirectUrl': MOMO_RETURN_URL,
		'ipnUrl': MOMO_IPN_URL,
		'lang': lang,
		'extraData': extraData,
		'requestType': requestType,
		'signature': signature,
        'orderGroupId': orderGroupId,
        'autoCapture': autoCapture
        
	}
    data = json.dumps(data)
    clen = len(data)
    response = requests.post(MOMO_ENDPOINT, data=data, headers={'Content-Type': 'application/json', 'Content-Length': str(clen)})
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
    vnp_ExpireDate = (datetime.now() + timedelta(minutes=10)).strftime('%Y%m%d%H%M%S')
    inputData = {
        'vnp_Version': '2.1.0',
        'vnp_Command': 'pay',
        'vnp_TmnCode': VNP_TMNCODE,
        'vnp_Amount': vnp_Amount,
        'vnp_CurrCode': 'VND',
        'vnp_TxnRef': vnp_TxnRef,
        'vnp_OrderInfo': vnp_OrderInfo,
        'vnp_OrderType': 'other',
        'vnp_Locale': 'vn',
        'vnp_ReturnUrl': VNP_RETURN_URL,
        'vnp_IpAddr': vnp_IpAddr,
        'vnp_CreateDate': vnp_CreateDate,
        'vnp_ExpireDate': vnp_ExpireDate
    }
    sortedData = sorted(inputData.items())
    
    # Build the query string
    queryString = '&'.join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sortedData])
    
    # Calculate the secure hash
    secureHash = hmacsha512(VNP_HASH_SECRET, queryString)
    # Build the full URL
    vnp_PayUrl = f"{VNP_ENDPOINT}?{queryString}&vnp_SecureHash={secureHash}"
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
    hashValue = hmacsha512(VNP_HASH_SECRET, hasData)
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
		
	