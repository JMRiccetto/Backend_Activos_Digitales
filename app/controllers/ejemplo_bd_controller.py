from flask import Blueprint, jsonify
from app.services.ejemplo_bd_service import get_all_has

ejemplo_bp = Blueprint('ejemplo_bd', __name__)

@ejemplo_bp.route('/has', methods=['GET'])
def obtener_has():
    has = get_all_has()
    return jsonify(has)