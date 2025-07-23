from flask import Blueprint, jsonify
from app.services.hola_service import get_hola_mundo

hola_bp = Blueprint('hola', __name__)

@hola_bp.route('/hola-mundo', methods=['GET'])
def hola_mundo():
    mensaje = get_hola_mundo()
    return jsonify({'mensaje': mensaje}) 