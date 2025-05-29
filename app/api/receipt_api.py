from flask import Blueprint, jsonify,request
from app.models.receipt import Receipt
from app.storage.cache import Cache
from app.storage.user import User
from app.services.receipt_service import ReceiptService

process_bp = Blueprint("process",__name__)
points_bp = Blueprint("points",__name__)

@process_bp.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt_json = request.json
    receipt:Receipt = Receipt.create_receipt(receipt_json)
    user:User = Cache.get_user_cache()
    user.receipt = receipt

    return jsonify({"id":user.session_id})

@points_bp.route('/receipts/<id>/points',methods = ['GET'])
def get_points(id):
    user:User = Cache.get_user_cache(id)
    receipt_service:ReceiptService = ReceiptService(user.receipt)
    user.points = receipt_service.calculate_total_points()
    return jsonify({"points":user.points})

    