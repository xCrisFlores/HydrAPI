import json
from flask import Blueprint, jsonify
from flask_sock import Sock
from app.services.consumption_service import ConsumptionService

consumption_bp = Blueprint('consumption_bp', __name__)

@consumption_bp.route('/consumption', methods=['GET'])
def get_all():
    """Obtener todos los consumos."""
    consumptions = ConsumptionService.get_all()
    return jsonify([{
        'id': consumption.id,
        'consumption': consumption.consumption,
        'time_active': consumption.time_active,
        'date': consumption.date.isoformat(),
        'user_id': consumption.user_id,
        'sensor_id': consumption.sensor_id
    } for consumption in consumptions]), 200

@consumption_bp.route('/consumption/<int:id>', methods=['GET'])
def get_consumption(id):
    """Obtener un consumo por ID."""
    consumption = ConsumptionService.get_by_id(id)
    if not consumption:
        return jsonify({'error': 'Consumo no encontrado'}), 404
    return jsonify({
        'id': consumption.id,
        'consumption': consumption.consumption,
        'time_active': consumption.time_active,
        'date': consumption.date.isoformat(),
        'user_id': consumption.user_id,
        'sensor_id': consumption.sensor_id
    }), 200

