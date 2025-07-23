from flask import Blueprint, jsonify
from app.services.segundo_service import get_segundo_endpoint

segundo_bp = Blueprint('segundo', __name__)

@segundo_bp.route('/segundo-endpoint', methods=['GET'])
def segundo_endpoint():
    mensaje = get_segundo_endpoint()
    return jsonify({'mensaje': mensaje}) 