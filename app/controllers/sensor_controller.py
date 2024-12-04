from flask import Blueprint, jsonify, request
from services.sensor_service import SensorService

sensor_bp = Blueprint('sensor_bp', __name__)

@sensor_bp.route('/sensors', methods=['GET'])
def get_all():
    """Obtiene todos los sensores."""
    sensors = SensorService.get_all()
    return jsonify([{
        'id': sensor.id,
        'name': sensor.name,
        'user_id': sensor.user_id,
        'real_time_cons': sensor.real_time_cons
    } for sensor in sensors]), 200

@sensor_bp.route('/sensors/<int:id>', methods=['GET'])
def get_sensorr(id):
    sensor = SensorService.get_by_id(id)
    if not sensor:
        return jsonify({'error': 'Sensor no encontrado'}), 404
    return jsonify({
        'id': sensor.id,
        'name': sensor.name,
        'user_id': sensor.user_id,
        'real_time_cons': sensor.real_time_cons
    }), 200

