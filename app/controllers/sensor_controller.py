from flask import Blueprint, jsonify, request
from app.services.sensor_service import SensorService

sensor_bp = Blueprint('sensor_bp', __name__)

@sensor_bp.route('/sensors', methods=['GET'])
def get_all():
    sensors = SensorService.get_all()
    return jsonify([{
        'id': sensor.id,
        'name': sensor.name,
        'user_id': sensor.user_id,
        'real_time_cons': sensor.real_time_cons
    } for sensor in sensors]), 200

@sensor_bp.route('/sensors/<int:id>', methods=['GET'])
def get_sensor(id):
    sensor = SensorService.get_by_id(id)
    if not sensor:
        return jsonify({'error': 'Sensor no encontrado'}), 404
    return jsonify({
        'id': sensor.id,
        'name': sensor.name,
        'user_id': sensor.user_id,
        'real_time_cons': sensor.real_time_cons
    }), 200

@sensor_bp.route('/sensors', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'name' not in data or 'user_id' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400
    new_sensor = SensorService.create_resource(data)
    return jsonify({
        'name': new_sensor.name,
        'user_id': new_sensor.user_id
    }), 201

@sensor_bp.route('/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    data = request.json
    updated = SensorService.update_resource(sensor_id, data)
    if not updated:
        return jsonify({'error': 'Sensor no encontrado'}), 404
    return jsonify({
       "name": updated.name
    }), 200

@sensor_bp.route('/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_user(sensor_id):
    deleted_user = SensorService.delete_resource(sensor_id)
    if not deleted_user:
        return jsonify({'error': 'Sensor no encontrado'}), 404
    return jsonify({'message': 'Sensor eliminado'}), 2
